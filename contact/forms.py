from django import forms
from django.core.mail import EmailMessage, send_mail
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=True,
    )
    email = forms.EmailField(
        max_length=255,
        required=True,
    )
    subject = forms.CharField(
        max_length=255,
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
    )

    def send_email(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            email = self.cleaned_data['email']
            subject = self.cleaned_data['subject']
            message = self.cleaned_data['message']
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
