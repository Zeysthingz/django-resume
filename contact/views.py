from core.models import DocumentModel
from django.http import JsonResponse
from django.shortcuts import render



# contact page
def contacts(request):
    documents=DocumentModel.objects.all().order_by('order')
    context = {
        'documents':documents,
    }
    return render(request, 'contact.html', context)

def contact_form(request):
    context = {
        'success': True,
        'message': 'Thank you for your message. I will get back to you soon.',
    }
    return JsonResponse(context)
