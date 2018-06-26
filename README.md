# Prometheus exporter for RQ

[RQ](http://python-rq.org/) (Redis Queue) is a simple Python library for queueing jobs. And this project aims to expose its metrics to [Prometheus](https://prometheus.io/).

## Build & Usage

Build the docker container
```
docker build -t rq-prometheus-exporter .
```

Run the docker container
```
docker run -it --rm -p 4567:8000 rq-prometheus-exporter
```
where `4567` is the port on docker host you'd like to expose exporter service to

## Development & Testing


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
