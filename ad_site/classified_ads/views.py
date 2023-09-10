from django.shortcuts import render, get_object_or_404
from .models import Ad
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'classified_ads/index.html'
    context_object_name = 'latest_ads_list'

    def get_queryset(self):
        """Return the last 10 published questions."""
        return Ad.objects.order_by("-date_posted")[:10]


class DetailView(generic.DetailView):
    model = Ad
    template_name = 'classified_ads/detail.html'
