from django.shortcuts import render, get_object_or_404
from .models import Ad, Comment
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse


class IndexView(generic.ListView):
    template_name = 'classified_ads/index.html'
    context_object_name = 'latest_ads_list'

    def get_queryset(self):
        """Return the last 10 published questions."""
        return Ad.objects.order_by("-date_posted")[:10]


class DetailView(generic.DetailView):
    model = Ad
    template_name = 'classified_ads/detail.html'


def comment(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    new_comment = Comment(parent_ad=ad,
                          comment_text=request.POST["comment"],
                          date_posted=timezone.now(),
                          user=request.POST["user"])
    new_comment.save()
    ad.comment_set.add(new_comment)
    return HttpResponseRedirect(reverse('classified_ads:detail', args=(ad.id,)))
