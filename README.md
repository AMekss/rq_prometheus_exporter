# Prometheus exporter for RQ

[![Build Status](https://travis-ci.org/AMekss/rq_prometheus_exporter.svg?branch=master)](https://travis-ci.org/AMekss/rq_prometheus_exporter)

[RQ](http://python-rq.org/) (Redis Queue) is a simple Python library for queueing jobs. And this project aims to expose its metrics to [Prometheus](https://prometheus.io/).

## Build & Usage

#### Build it
```
docker build -t rq-prometheus-exporter .
```

#### Pull it from [dockerhub](https://hub.docker.com/r/amekss/rq-prometheus-exporter/)
```
docker pull amekss/rq-prometheus-exporter:stable
```

#### Run it
There is `RQ_REDIS_URI` environment variable available to setup URL for the redis used by RQ
```
docker run -it --rm -p 4567:8000 rq-prometheus-exporter
```
where `4567` is the port on docker host you'd like to expose exporter service to.

**Note:** For more details on how to use `docker` please head to the official [documentation of Docker](https://docs.docker.com/)

## Available metrics
```
rq_enqueued_jobs        gauge   The total number of enqueued jobs (labels: queue_name)
rq_workers              gauge   The number of workers performing jobs (labels: name, queues, state)
```

You can skip scraping `rq_workers` metric by setting the environment variable
`RQPE_SCRAPE_WORKERS` to anything else then `true`, `yes`, `t` or `1`. This is
useful in the scenarios you are running RQ workers on preemtible nodes where
new spawned workers get new unique hostnames each time.

While it's good enough for setting up basic monitoring and alerting in Prometheus, in future would be good to comeback to this and check how to extend it with more metrics

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
