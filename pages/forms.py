from django.forms import ModelForm
from django.forms import TextInput, Textarea
from .models import Contact


class ContactForm(ModelForm):
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
