FROM python:3.9.12

COPY . /opt/ocrmypdf-leak
WORKDIR /opt/ocrmypdf-leak

RUN apt-get update -y
RUN apt-get  install software-properties-common -y
RUN apt-get update -y && apt-get -y install qpdf poppler-utils libpoppler-dev libpoppler-cpp-dev ffmpeg libsm6 libxext6 ghostscript

RUN pip install ocrmypdf memory-profiler
