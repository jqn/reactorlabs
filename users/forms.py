# users/forms.py
from django import forms
from allauth.account.forms import SignupForm


class CustomUserCreationForm(SignupForm):
        
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('@reactorlabs.studio'):
            raise forms.ValidationError("Please enter a valid email")
        return email

