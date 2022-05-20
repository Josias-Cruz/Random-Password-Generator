FROM python:3.11-rc-slim-buster

ARG appname=random-password-generator

WORKDIR /random-password-generator

COPY src/* ./src/
COPY requirements.txt ./

RUN pip install -U \
    pip \
    setuptools \
    wheel

RUN pip install -r requirements.txt





