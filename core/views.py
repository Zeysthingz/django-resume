from django.shortcuts import render
from .models import GeneralSetting


# index page

def index(request):
    site_title = GeneralSetting.objects.get(site_title='site_title').parameters
    site_keywords= GeneralSetting.objects.get(site_title='site_keywords').parameters
    site_description = GeneralSetting.objects.get(site_title='site_description').parameters
    home_banner_title = GeneralSetting.objects.get(site_title='home_banner_title').parameters
    home_banner_job = GeneralSetting.objects.get(site_title='home_banner_job').parameters
    home_banner_description = GeneralSetting.objects.get(site_title='home_banner_description').parameters
    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_title': home_banner_title,
        'home_banner_job':home_banner_job,
        'home_banner_description':home_banner_description,
    }
    return render(request, 'index.html', context)
