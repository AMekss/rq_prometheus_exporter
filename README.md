# Prometheus exporter for RQ

[RQ](http://python-rq.org/) (Redis Queue) is a simple Python library for queueing jobs. And this project aims to expose its metrics to [Prometheus](https://prometheus.io/).

## Build & Usage

#### Build it
```
docker build -t rq-prometheus-exporter .
```

#### Run it
There is `RQ_REDIS_URI` environment variable available to setup URL for the redis used by RQ
```
docker run -it --rm -p 4567:8000 rq-prometheus-exporter
```
where `4567` is the port on docker host you'd like to expose exporter service to.

**Note:** For more details on how to use `docker` please head to the official [documentation of Docker](https://docs.docker.com/)

## Development & Testing

#### Build development environment
```
docker-compose build
```

#### Run it in development mode
```
docker-compose up
```
Container will be exposed on port `4567` of docker host machine and hot reloading is enabled so all changes to code have to be seen even without restarting gunicorn process or container (it might take a few seconds for process to reload though)

#### Running tests
```
docker-compose run --rm exporter pytest
```

**Note:** For more details on how to use `docker-compose` please head to the official [documentation of Docker Compose](https://docs.docker.com/compose/)

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
