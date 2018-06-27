#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker tag amekss/rq-prometheus-exporter:latest amekss/rq-prometheus-exporter:stable
docker push amekss/rq-prometheus-exporter:stable
