#pull official base image
FROM python:3.10-slim

RUN apt-get update

# -y say yes to all question when installing
RUN apt-get install python3-dev build-essential -y


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV=/opt/venv
# pip requirements
RUN pip install --upgrade pip

# creates venv under opt directory
RUN pip install virtualenv && python -m virtualenv $VIRTUAL_ENV

# coppy locaded root directory  requirements.txt under temp directory
ADD ./requirements.txt /tmp/requirements.txt

# install requirements.txt
RUN pip install -r /tmp/requirements.txt

# coppy all files under srv directory
COPY . /srv/app


# Linux inside docker gonna use python inside venv

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# set working directory

WORKDIR /srv/app

