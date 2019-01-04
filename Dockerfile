#FROM python:3.7-alpine3.7
FROM selenium/node-chrome

USER root 

#RUN apt-get update -qqy 
RUN apt-get -qy update && apt-get install -y "python-pip" 

RUN find / -name chromedriver 
	install pip

#RUN apt-get -qqy update \ 
#    && apt-get -qqy install \
#   python

EXPOSE 4444 
COPY --chown=root:root . /home/python/src/
WORKDIR /home/python/src
RUN pip install selenium
RUN python3 ./use_whatsapp.py
