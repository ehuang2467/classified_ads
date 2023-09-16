from django.db import models


class Postable(models.Model):
    text = models.CharField(max_length=1000)
    date_posted = models.DateTimeField()
    user = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.text


class Ad(models.Model):
    BUY = "Buy"
    SELL = "Sell"
    ad_type_choices = [
        (BUY, "Buy"),
        (SELL, "Sell")
    ]
    ad_text = models.CharField(max_length=1000)
    date_posted = models.DateTimeField()
    ad_type = models.CharField(
        max_length=4, choices=ad_type_choices)
    user = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.ad_text


class Comment(models.Model):
    class Meta:
        ordering = ['date_posted']
    parent_ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=1000)
    date_posted = models.DateTimeField()
    user = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.comment_text
