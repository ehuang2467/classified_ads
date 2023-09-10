from django.urls import path
from . import views

app_name = "classified_ads"

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:ad_id>/", views.detail, name="detail")
]
