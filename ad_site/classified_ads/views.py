from django.shortcuts import render, get_object_or_404
from .models import Ad


def index(request):
    latest_ads_list = Ad.objects.order_by("-date_posted")[:10]
    context = {"latest_ads_list": latest_ads_list}
    return render(request, "classified_ads/index.html", context)


def detail(request, ad_id):
    context = {"parent_ad": get_object_or_404(Ad, pk=ad_id)}
    return render(request, 'classified_ads/detail.html', context)
