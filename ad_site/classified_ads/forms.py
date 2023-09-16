from django import forms
from django.forms import ModelForm
from .models import Ad, Comment
from django.contrib.auth.models import User


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


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        help_texts = {
            "username": "",
        }
