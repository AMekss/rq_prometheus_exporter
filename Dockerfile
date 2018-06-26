FROM python:3.6-alpine3.7

ENV LANG C.UTF-8
WORKDIR /app

COPY requirements.txt .

RUN apk update && apk add --no-cache build-base \
  && pip install -r requirements.txt \
  && apk del --purge build-base

COPY . ./

CMD ["gunicorn", "-b 0.0.0.0:8000", "-w 2", "api:api"]
