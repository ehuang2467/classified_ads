from django import forms
from django.forms import ModelForm
from .models import Ad


class AdForm(ModelForm):
    class Meta:
        model = Ad
        exclude = ["date_posted", "user",]


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
