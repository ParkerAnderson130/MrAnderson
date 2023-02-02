from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    content = forms.CharField (required=True, widget=forms.Textarea)

    def get_content(self):
        cl_data = super().clean()

        name = cl_data.get('name')
        from_email = cl_data.get('email')
        subject = cl_data.get('content')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_content()

        send_mail(
            subject=subject,
            message=msg,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [settings.RECIPIENT_ADDRESS]
        )