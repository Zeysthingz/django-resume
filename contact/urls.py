from django.urls import path
from .views import contact_form
urlpatterns = [

    # home page
    path('contact_form', contact_form, name='contact_form'),
]
