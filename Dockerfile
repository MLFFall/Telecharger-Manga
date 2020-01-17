FROM ubuntu:latest

RUN apt -y update
RUN apt -y install python3
RUN apt -y install python3-pip

RUN pip3 install beautifulsoup4
RUN pip3 install requests
RUN pip3 install pillow
COPY * /usr/src/app/downloadManga/

RUN chmod -R 777 /usr/src/app/downloadManga/*

RUN echo "PATH=/usr/src/app/downloadManga:$PATH" >> ~/.bashrc

