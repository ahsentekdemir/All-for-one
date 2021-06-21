FROM python:3.9
ENV PYTHONBUFFERED 1
WORKDIR /app_
COPY ./requirements.txt /app_/requirements.txt
RUN pip install -r requirements.txt
COPY . /app_

CMD python services/main.py
