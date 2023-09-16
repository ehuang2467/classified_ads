from django.db import models


class Postable(models.Model):
    text = models.CharField(max_length=1000)
    date_posted = models.DateTimeField()
    user = models.CharField(max_length=30)

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


class Comment(Postable):
    parent_ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_posted']
