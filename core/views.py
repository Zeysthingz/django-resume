from django.shortcuts import render
from .models import GeneralSetting, ImageSetting


# index page

def index(request):
    site_title = GeneralSetting.objects.get(site_title='site_title').parameters
    site_keywords = GeneralSetting.objects.get(site_title='site_keywords').parameters
    site_description = GeneralSetting.objects.get(site_title='site_description').parameters
    home_banner_title = GeneralSetting.objects.get(site_title='home_banner_title').parameters
    home_banner_job = GeneralSetting.objects.get(site_title='home_banner_job').parameters
    home_banner_description = GeneralSetting.objects.get(site_title='home_banner_description').parameters

    # Images
    home_banner_image = ImageSetting.objects.get(name='home_banner_image').file
    site_fav_icon = ImageSetting.objects.get(name='site_fav_icon').file
    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_title': home_banner_title,
        'home_banner_job': home_banner_job,
        'home_banner_description': home_banner_description,
        'home_banner_image': home_banner_image,
        'site_fav_icon': site_fav_icon,
    }
    return render(request, 'index.html', context)
