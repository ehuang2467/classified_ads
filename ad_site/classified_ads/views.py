from django.shortcuts import render, get_object_or_404
from .models import Ad, Comment
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth  # authenticate, login, logout, get_user


class IndexView(generic.ListView):
    template_name = 'classified_ads/index.html'
    context_object_name = 'latest_ads_list'

    def get_queryset(self):
        """Return the last 10 published ads."""
        return Ad.objects.order_by("-date_posted")[:10]


class DetailView(generic.DetailView):
    model = Ad
    template_name = 'classified_ads/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['comment_list'] = Ad.objects.all()
        return context


def comment(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    new_comment = Comment(parent_ad=ad,
                          text=request.POST["comment"],
                          date_posted=timezone.now(),
                          user=auth.get_user(request))
    new_comment.save()
    ad.comment_set.add(new_comment)
    return HttpResponseRedirect(reverse('classified_ads:detail', args=(ad.id,)))


def post(request):
    image = request.FILES["image"]
    new_ad = Ad(text=request.POST["post"],
                ad_type=request.POST["ad_type"],
                date_posted=timezone.now(),
                user=auth.get_user(request),
                image=image)
    new_ad.save()
    return HttpResponseRedirect(reverse('classified_ads:index'))


def login_register(request):
    return render(request, "classified_ads/login_register.html", {})


def register(request):

    User.objects.create_user(username=request.POST["username"],
                             password=request.POST["password"])
    return HttpResponseRedirect(reverse('classified_ads:index'))


def login_view(request):
    attempted_user = auth.authenticate(username=request.POST["username"],
                                       password=request.POST["password"])
    login_is_successful = attempted_user is not None
    if login_is_successful:
        auth.login(request, attempted_user)
        return HttpResponseRedirect(reverse('classified_ads:index'))
    else:
        return HttpResponse("Login failed")


def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('classified_ads:index'))
