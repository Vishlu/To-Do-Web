from django import forms
from .models import User


class Studentregistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']