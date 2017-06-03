from django import forms
from django.contrib.auth.models import User

# from .models import Album, Song


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

