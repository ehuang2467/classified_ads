from .models import Ad
from rest_framework import serializers


class AdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ad
        fields = ["text", "date_posted", "ad_type"]
