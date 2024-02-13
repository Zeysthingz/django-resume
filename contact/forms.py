from django import forms
from .tasks import send_feedback_email_task


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
            # .apply_async() is used to call the task asynchronously
            send_feedback_email_task.delay(
                name=self.cleaned_data['name'],
                email=self.cleaned_data['email'],
                subject=self.cleaned_data['subject'],
                message=self.cleaned_data['message'],
            )
