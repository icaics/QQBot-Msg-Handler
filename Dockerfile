FROM python:3.5

RUN pip install qqbot

COPY qqbot.sh /
