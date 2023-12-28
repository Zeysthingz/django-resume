from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.http import JsonResponse
from contact.forms import ContactForm
from contact.models import Messages
from .models import (
    DocumentModel,
    EducationModel,
    ExperienceModel,
    GeneralSetting,
    ImageSetting,
    SkillModel,
    SocialMediaModel,
)


def get_general_settings(parameter):
    obj = None
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameters
    except:
        obj = ''
    return obj


def get_image_settings(parameter):
    img_obj = None
    try:
        img_obj = ImageSetting.objects.get(name=parameter).file
    except:
        img_obj = ''
    return img_obj


def layout(request):
    site_title = get_general_settings('site_title')
    site_keywords = get_general_settings('site_keywords')
    site_description = get_general_settings('site_description')
    home_banner_title = get_general_settings('home_banner_title')
    home_banner_job = get_general_settings('home_banner_job')
    home_banner_description = get_general_settings('home_banner_description')

    # Images
    home_banner_image = get_image_settings('home_banner_image')
    site_fav_icon = get_image_settings('site_fav_icon')

    # Documents
    documents = DocumentModel.objects.all().order_by('order')
    context = {
        'documents': documents,
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_title': home_banner_title,
        'home_banner_job': home_banner_job,
        'home_banner_description': home_banner_description,
        'home_banner_image': home_banner_image,
        'site_fav_icon': site_fav_icon,
    }
    return context


# index page
def index(request):


    # Skills
    skills = SkillModel.objects.all().order_by('order')

    # Experiences
    experiences = ExperienceModel.objects.all().order_by('-start_date')

    # Education
    educations = EducationModel.objects.all().order_by('-start_date')

    # Social Media
    social_medias = SocialMediaModel.objects.all().order_by('order')

    # Contact Form
    contact_form = ContactForm()
    if request.method == 'POST':
        context = {
            'success': False,
            'message': '',
        }
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

            # creates an object in the database
            Messages.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )
            contact_form.send_email()
            context['success'] = True
            context['message'] = 'Thank you for your message. I will get back to you soon.'
        else:
            context['success'] = False
            context['message'] = 'Could not send message. Please try again later.'
        return JsonResponse(context)


    context = {
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'contact_form': contact_form,
        'social_medias': social_medias,
    }
    return render(request, 'index.html', context)


def redirect_urls(request, slug):
    document = get_object_or_404(DocumentModel, slug=slug)
    if document:
        return redirect(document.file.url)
