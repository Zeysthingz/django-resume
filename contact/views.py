
from django.http import JsonResponse

def contact_form(request):
    context = {
        'success': True,
        'message': 'Thank you for your message. I will get back to you soon.',
    }
    return JsonResponse(request,context)
