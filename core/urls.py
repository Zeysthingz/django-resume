

from django.urls import path
from .views import index, redirect_urls

urlpatterns = [

    # home page
    path('', index, name='index'),

    # redirect urls
    path('<slug>/', redirect_urls, name='redirect_urls'),

]
