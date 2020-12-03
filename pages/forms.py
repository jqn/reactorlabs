from django.forms import ModelForm
from django.forms import TextInput, Textarea
from .models import Contact
from django.core.mail import send_mail


class ContactForm(ModelForm):
    def send_email(self):
        pass
        # # send email using the self.cleaned_data dictionary
        # subject = f"New email from {self.cleaned_data['name']}"
        # message = f"Contact Name: {self.cleaned_data['name']}\n" \
        #     f"Contact Phone Number: {self.cleaned_data['phone']}\n" \
        #     f"Contact Email: {self.cleaned_data['email']}\n\n" \
        #     f"{self.cleaned_data['message']}"
        # sender = 'noreply@reactorlabs.studio'
        # recipient_list = ['jqngl@icloud.com']

        # send_mail(
        #     subject,
        #     message,
        #     sender,
        #     recipient_list,
        #     fail_silently=False,
        # )

    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "name",
                    "type": "text",
                    "placeholder": "Your Name *",
                    "required": True,
                    "data-validation-required-message": "Please enter your name.",
                }
            ),
            "email": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "type": "email",
                    "placeholder": "Your Email *",
                    "required": True,
                    "data-validation-required-message": "Please enter your email address.",
                }
            ),
            "phone": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "phone",
                    "type": "tel",
                    "placeholder": "Your Phone *",
                    "required": True,
                    "data-validation-required-message": "Please enter your phone number.",
                }
            ),
            "message": Textarea(
                attrs={
                    "class": "form-control",
                    "id": "message",
                    "placeholder": "Your Message *",
                    "required": True,
                    "data-validation-required-message": "Please enter a message.",
                    "rows": 8
                }
            )
        }
