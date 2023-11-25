
from django.urls import path, include
from .views import index, contacts

urlpatterns = [

    # home page
    path('', index, name='index'),

    # contact page
    path('contacts/', contacts, name='contacts'),
]
