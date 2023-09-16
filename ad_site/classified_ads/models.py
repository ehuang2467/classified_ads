from django.db import models
from django.contrib.auth import models as auth_models
from django.core.files.storage import FileSystemStorage


class Postable(models.Model):
    text = models.CharField(max_length=1000)
    date_posted = models.DateTimeField()
    # user = models.CharField(max_length=30)
    user = models.ForeignKey(
        auth_models.User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.text


class Ad(Postable):
    BUY = "Buy"
    SELL = "Sell"
    ad_type_choices = [
        (BUY, "Buy"),
        (SELL, "Sell")
    ]
    ad_type = models.CharField(
        max_length=4, choices=ad_type_choices)
    image = models.ImageField(
        null=True, default=None)

    def has_image(self):
        return not self.image


class Comment(Postable):
    parent_ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_posted']
