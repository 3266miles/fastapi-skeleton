FROM python:3.8-slim-buster
LABEL maintainer="Slide - dan@littleatlas.xyz"

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get -qq update && \
    apt-get install --no-install-recommends -y -qq gcc python3-pip libpq-dev python3-dev  \
    default-libmysqlclient-dev build-essential ca-certificates && \
    pip3 install -r requirements.txt

COPY . ./

USER 1005

ENTRYPOINT ["ddtrace-run", "hypercorn", "api.main:app", "--config", "hypercorn-config.toml"]