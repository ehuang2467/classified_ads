from .models import Ad
from rest_framework import serializers
from django.contrib.auth.models import User


class AdSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Ad
        fields = ["text", "date_posted", "ad_type", "user"]
