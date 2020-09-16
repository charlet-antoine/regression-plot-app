# regression-plot-app
This project demonstrates how to expose a simple flask server with docker.


# To try the demo: 
```
git clone https://github.com/charlet-antoine/regression-plot-app.git
cd regression-plot-app.git
docker build --tag flaskregapp .
docker run -it --name 'flaskplotapp' -p 5000:5000 flaskregapp:latest
```
