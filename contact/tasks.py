from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from celery import shared_task


@shared_task()
def send_feedback_email_task(name, email, subject, message):
    name = name
    email = email
    subject = subject
    message = message
    message_context = 'Message received.\n\n' \
                      'Name: %s\n' \
                      'Subject: %s\n' \
                      'Email: %s\n' \
                      'Message: %s' % (name, subject, email, message)

    # Send acknowledgment email to the user
    ack_subject = "Message Received"
    ack_message = (
        f"Dear {name},\n\n"
        "Thank you for contacting me! I have received your message and will get back to you soon.\n\n"
        "Best regards,\n Zeynep AKBALIK\n\n"
    )
    send_mail(ack_subject, ack_message, settings.DEFAULT_FROM_EMAIL, [email])

    # Send email here to user
    email = EmailMessage(
        subject,
        message_context,
        # us
        to=[settings.DEFAULT_FROM_EMAIL],
        # user
        reply_to=[email],
    )
    email.send()
