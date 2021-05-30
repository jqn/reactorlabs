# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _


from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'editor', 'password1', 'password2',)
        exclude = ['editor', ]
        help_texts = {
            'username': None,
        }
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('@reactorlabs.studio'):
            raise forms.ValidationError("Please enter a valid email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email alrealy exists.")
        return email


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'editor',)
