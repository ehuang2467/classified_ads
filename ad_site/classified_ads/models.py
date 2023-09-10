from django.db import models


class Ad(models.Model):
    BUY = "Buy"
    SELL = "Sell"
    ad_type_choices = [
        (BUY, "Buy"),
        (SELL, "Sell"),
        ("None", "None - Placeholder")
    ]
    ad_text = models.CharField(max_length=200)
    date_posted = models.DateTimeField('date posted')
    ad_type = models.CharField(
        max_length=4, choices=ad_type_choices)

# Create your models here.
