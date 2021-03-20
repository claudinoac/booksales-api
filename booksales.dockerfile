FROM python:3.7-alpine

RUN mkdir -p /code
WORKDIR /code

RUN apk add --no-cache --upgrade --virtual .build-deps postgresql-dev gcc g++ linux-headers musl-dev
COPY ./requirements /code/requirements
RUN pip install -r requirements/development.txt
RUN apk del .build-deps && apk add postgresql
EXPOSE 9090
