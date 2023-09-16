from django import forms
from django.forms import ModelForm
from .models import Ad


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ["ad_type", "text",  "image"]
        labels = {
            "text": "Ad Description",
            "image": "Image (optional)",
        }
        # help_texts = {
        #     "image": "optional"
        # }


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
