from django import forms
from django.forms import ModelForm
from .models import Ad, Comment


class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ["ad_type", "text",  "image"]
        labels = {
            "text": "Ad Description",
            "image": "Image (optional)",
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        labels = {
            "text": "Comment",
        }


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
