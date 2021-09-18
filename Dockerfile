FROM python:3.7-alpine
MAINTAINER Nick Iasceri

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user