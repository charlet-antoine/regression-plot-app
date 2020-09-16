from flask import Flask, send_file
from plotdata import regression_plot

app = Flask(__name__)

@app.route('/', methods=['GET'])
def reg_plot():
    image = regression_plot()
    return send_file(image, attachment_filename='regress.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)