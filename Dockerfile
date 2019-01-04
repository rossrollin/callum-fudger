#FROM python:3.7-alpine3.7
FROM selenium/node-chrome

USER root 

RUN apt-get -qy update && apt-get install -y "python-pip" 

COPY --chown=root:root . /home/python/src/
WORKDIR /home/python/src
RUN pip install selenium
RUN python3 ./use_whatsapp.py
