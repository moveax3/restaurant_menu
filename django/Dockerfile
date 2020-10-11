FROM python:3.9-alpine
RUN apk add build-base
RUN apk add linux-headers
RUN apk add postgresql-dev
COPY python-requirements.txt /
RUN pip3 install -r /python-requirements.txt
RUN mkdir /app
WORKDIR /app