from django.db import models
from django import  forms
# Create your models here.

class UserFrom(forms.Form):
    username = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput)
    password_1 = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput)
