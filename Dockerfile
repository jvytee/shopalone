FROM python:3.8-alpine

RUN apk update
RUN apk add python3-dev libpq build-base

COPY . /opt/shopalone
RUN pip install -r /opt/shopalone/requirements.txt

RUN adduser gunicorn
USER gunicorn
WORKDIR /opt/shopalone/src

CMD gunicorn -w 4 shopalone:app
