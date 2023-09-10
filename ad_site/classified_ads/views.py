from django.shortcuts import render


from .models import Ad


def index(request):
    latest_ads_list = Ad.objects.order_by("-date_posted")[:10]
    context = {"latest_ads_list": latest_ads_list}
    return render(request, "classified_ads/index.html", context)
