from django.shortcuts import render,redirect,get_object_or_404
from .models import (
    DocumentModel,
    EducationModel,
    ExperienceModel,
    GeneralSetting,
    ImageSetting,
    SkillModel,
    SocialMediaModel,
)


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

    # Skills
    skills = SkillModel.objects.all().order_by('order')

    # Experiences
    experiences = ExperienceModel.objects.all().order_by('-start_date')

    # Education
    educations = EducationModel.objects.all().order_by('-start_date')

    # Social Media
    social_medias= SocialMediaModel.objects.all().order_by('order')

    # Documents
    documents=DocumentModel.objects.all().order_by('order')


    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_title': home_banner_title,
        'home_banner_job': home_banner_job,
        'home_banner_description': home_banner_description,
        'home_banner_image': home_banner_image,
        'site_fav_icon': site_fav_icon,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'social_medias': social_medias,
        'documents':documents,
    }
    return render(request, 'index.html', context)


def redirect_urls(request,slug):
    document=get_object_or_404(DocumentModel,slug=slug)
    if document:
        return redirect(document.file.url)