from django.http import JsonResponse
from django.shortcuts import render
from .models import Messages


# contact page
def contacts(request):
    context = {
    }
    return render(request, 'contact.html', context)


def contact_form(request):
    if request.method == 'POST':
        print(149742975902580)
        print(149742975902580)
        print(149742975902580)
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        success = True
        messages = 'Thank you for your message. I will get back to you soon.',

        # creates an object in the database
        Messages.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

    else:
        success = False
        messages = 'Could not send message. Please try again later.'
    context = {
        'success': success,
        'message': messages,
    }
    return JsonResponse(context)
