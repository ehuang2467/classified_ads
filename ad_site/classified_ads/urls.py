from django.urls import path
from . import views

app_name = "classified_ads"

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("post/", views.post_ad, name="post"),
    path("login_register/", views.login_register, name="login_register"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
