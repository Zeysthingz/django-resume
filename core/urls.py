
from django.urls import path, include
from .views import index

urlpatterns = [

    # home page
    path('', index, name='index'),
]
