from django.urls import path
from . import views

app_name = "classified_ads"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/comment/", views.comment, name="comment"),
    path("post/", views.post, name="post"),
    path("login_register/", views.login_register, name="login_register"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login")
]
