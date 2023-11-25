from django.urls import path
from .views import contacts, contact_form
urlpatterns = [
    # contact page
    path('contacts/', contacts, name='contacts'),

    # contact form
    path('contact_form', contact_form, name='contact_form'),
]
