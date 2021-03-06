FROM python:3.9
ENV PYTHONBUFFERED 1
WORKDIR /app_
# RUN apt update && \
# 	apt install gcc libpq-dev -y
COPY requirements.txt /app_/requirements.txt
RUN pip install -r requirements.txt
COPY . /app_

