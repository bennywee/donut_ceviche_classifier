FROM python:3.8-slim-buster AS dev

COPY requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /classifier