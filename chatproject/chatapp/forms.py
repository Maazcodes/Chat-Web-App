from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from captcha.fields import CaptchaField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class MyForm(forms.Form):
    """Captcha Form"""
    captcha = CaptchaField()

class UserForm(ModelForm):
    """Form to edit user details."""

    class Meta:
        model = User
        fields = ['username','email', 'first_name','last_name']