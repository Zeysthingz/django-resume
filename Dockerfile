# pull official base image
FROM python:3.10-slim

RUN apt-get update

# Install PostgreSQL development libraries
RUN apt-get install libpq-dev -y
RUN apt-get install postgresql-client -y

RUN apt-get install python3-dev build-essential -y


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/venv

# pip requirements
RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

#gives permissions to sh
COPY entrypoint.sh /srv/entrypoint.sh
RUN sed -i 's/\r$//g' /srv/entrypoint.sh
RUN chmod +x /srv/entrypoint.sh

COPY . /srv/app
WORKDIR /srv/app

ENTRYPOINT ["/srv/entrypoint.sh"]
