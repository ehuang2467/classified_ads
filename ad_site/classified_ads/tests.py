from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import datetime
from .models import Ad


def create_ad(ad_type=Ad.BUY, ad_text="", days=0, user=""):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    now_plus_days = timezone.now() + datetime.timedelta(days=days)
    new_ad = Ad.objects.create(
        ad_text=ad_text, ad_type=ad_type, date_posted=now_plus_days, user=user)
    return new_ad


class AdIndexViewTests(TestCase):
    def test_no_ads(self):
        """
        If no ads exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('classified_ads:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No ads have been posted.")
        self.assertQuerysetEqual(response.context['latest_ads_list'], [])

    def test_ads(self):
        """
        If 2 ads exist, they are displayed and 
        in order of newest post to oldest post.
        """
        now_ad = create_ad(ad_text="now_ad", days=0)
        yesterday_ad = create_ad(ad_text="yesterday ad", days=-1)
        response = self.client.get(reverse('classified_ads:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_ads_list'],
                                 [now_ad, yesterday_ad])


class AdDetailViewTests(TestCase):
    def test_no_comments(self):
        """
        If no comments exist, no comments are displayed.
        """
        response = self.client.get(reverse('classified_ads:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No ads have been posted.")
        self.assertQuerysetEqual(response.context['latest_ads_list'], [])

    def test_ads(self):
        """
        If 2 ads exist, they are displayed and 
        in order of newest post to oldest post.
        """
        now_ad = create_ad(ad_text="now_ad", days=0)
        yesterday_ad = create_ad(ad_text="yesterday ad", days=-1)
        response = self.client.get(reverse('classified_ads:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_ads_list'],
                                 [now_ad, yesterday_ad])


# Create your tests here.
