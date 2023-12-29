# Personal Resume Web App

## About

The project is set on Docker for development server and set configurations for server and AWS S3 for production server.

Some features:

* Django Management Command


* **Docker** for continuous development server


* **Gunicorn** for running the Python application code


* **Nginx** for serving static content


* **/\<slug>/** : (_views.special_links_)  If path matches with 'name' field, it redirects to document(media) url which
  is resume pdf file



* **custom_storage:** There are 3 type of storages in purpose. Uploaded documents, images(from ImageSettings model) and
  all other media are uploads different locations. 3 type of storage managements are set for development and production
  separately.



* Amazon S3 integrations are ready.

## Installation

To start project,

1. First create a docker.env file from env.txt. Change&enter required parameters.


2. Start services at background:

   `docker-compose up -d --build`

## Django Management Commands

* Just to remind, session flushing command can be run periodically if the django_session table became huge.

*
    * Locally:

`docker-compose exec app python manage.py clearsessions`

*
    * In Production Server:

`docker compose run app_name python manage.py clearsessions`

* To upload static files to S3:

*
  * In Production Server:
  
`docker compose run app_name python manage.py collectstatic`
