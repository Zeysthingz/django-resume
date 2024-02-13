# Personal Resume Web App

## About

The project is set on Docker for development server and set configurations for  Nginx server and AWS S3 for production server.

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

*

    * Locally:

`docker-compose exec app python manage.py clearsessions`

*
    * In Production Server:

`docker compose run app_name python manage.py clearsessions`

To upload static files to S3:

*
  * In Production Server:
  
`docker compose run app_name python manage.py collectstatic`

## Google Recaptcha Integration
* Go to the reCAPTCHA website and sign in with your Google account.[recaptcha](https://www.google.com/recaptcha/about/)
* Click on the "+" button to create a new site.
* Choose "reCAPTCHA v3" as the type.
* Enter your domain under Domains.
* Accept the reCAPTCHA Terms of Service and click on the "Submit" button.
* You will get the Site Key and Secret Key.
* Add the keys to the docker.env file or settings.py file.
``` 
RECAPTCHA_SITE_KEY = 'your_site_key'
RECAPTCHA_SECRET= 'your_secret_key'
``` 

## Celery-Redis Integration
Celery is an asynchronous task queue/job queue based on distributed message passing. 
It is focused on real-time operation, but supports scheduling as well.
Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.

* pip install celery[redis]
* Add the following code to .env file or the settings.py file.
```
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
```
* Create a celery.py file in your Django app and add configurations related your app.
```
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

# Create a Celery instance and configure it using the settings from Django
celery_app = Celery('your_project')

# Load task modules from all registered Django app configs.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
celery_app.autodiscover_tasks()
```
* create a tasks.py file in your Django app define the task should be processed by Celery.
### Use Case task.py
```
@shared_task()
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "support@example.com",
        [email_address],
        fail_silently=False,
    )
```







