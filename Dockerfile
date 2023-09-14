FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /currency_converter

COPY requirements.txt ./
COPY . .

EXPOSE 8000

RUN pip install -r requirements.txt