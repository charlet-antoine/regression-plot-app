# regression-plot-app
This project demonstrate how to expose a simple flask server within a docker container

```
git clone https://github.com/charlet-antoine/regression-plot-app.git
cd regression-plot-app.git
docker build --tag flaskregapp .
docker run -it --name 'flaskplotapp' -p 5000:5000 flaskregapp:latest
```