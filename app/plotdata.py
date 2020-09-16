import pandas as pd
import seaborn as sns
import io
import matplotlib


matplotlib.use('agg')

def regression_plot():
    df = pd.read_csv('../data/data.csv')
    sns_plot = sns.regplot(x='Rainfall', y='Temperature', data=df)
    image = io.BytesIO()
    sns_plot.figure.savefig(image, format='png')
    image.seek(0)
    return image

if __name__ == '__main__':
    from PIL import Image
    image = regression_plot()
    im = Image.open(image)
    im.save('../data/regress.png', 'PNG')