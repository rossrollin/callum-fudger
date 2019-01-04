#FROM python:3.7-alpine3.7
FROM selenium/node-chrome

#RUN apt-get -qqy update \ 
#    && apt-get -qqy install \
#   python

EXPOSE 4444 
COPY --chown=root:root . /home/python/src/
WORKDIR /home/python/src/
RUN ./use_whatsapp.py
