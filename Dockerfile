FROM python:3.8-slim

COPY . /root/shopalone
RUN pip install /root/shopalone[server]
RUN rm -rf /root/shopalone

RUN adduser --system shopalone --group
USER shopalone

CMD gunicorn -b 0.0.0.0:8000 -w 4 shopalone.main:app
