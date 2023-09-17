from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import datetime
from .models import Ad, Comment
from django.contrib import auth


def create_ad(ad_type=Ad.BUY, text="", days=0, user=None):
    """
    Create an ad with the given parameters and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    now_plus_days = timezone.now() + datetime.timedelta(days=days)
    new_ad = Ad.objects.create(
        text=text, ad_type=ad_type, date_posted=now_plus_days, user=user)
    return new_ad


def create_comment(parent_ad, text="", days=0, user=None):
    """
    Create a comment with the given parameters and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    now_plus_days = timezone.now() + datetime.timedelta(days=days)
    new_comment = Comment.objects.create(
        parent_ad=parent_ad,
        text=text,
        date_posted=now_plus_days, user=user)
    return new_comment


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
        in order of newest post on top to oldest post on bottom.
        """
        now_ad = create_ad(text="now_ad", days=0)
        yesterday_ad = create_ad(text="yesterday ad", days=-1)
        response = self.client.get(reverse('classified_ads:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_ads_list'],
                                 [now_ad, yesterday_ad])


class AdDetailViewTests(TestCase):
    def test_no_comments(self):
        """
        If no comments exist, no comments are displayed.
        """
        ad = create_ad(text="ad")
        response = self.client.get(
            reverse('classified_ads:detail', kwargs={"pk": ad.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['ad'].comment_set.all(), [])

    def test_comments(self):
        """
        If 2 comments exist, they are displayed and
        in order of oldest comment on top to newest comment on botom.
        """
        ad = create_ad(text="ad")
        now_comment = create_comment(ad, text="now comment", days=0)
        yesterday_comment = create_comment(
            ad, text="yesterday comment", days=-1)
        response = self.client.get(
            reverse('classified_ads:detail', kwargs={"pk": ad.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['ad'].comment_set.all()),
                                 [yesterday_comment, now_comment])


class AuthTests(TestCase):
    def test_register_and_login(self):
        """
        Before registering and logging in, not authenticated user.
        After, is authenticated user.
        """
        self.assertNotIn('_auth_user_id', self.client.session)
        register_context = {"username": "fake_username",
                            "password": "fake_password"}
        self.client.post(
            reverse('classified_ads:register'), register_context
        )
        self.client.post(
            reverse('classified_ads:login'), register_context
        )
        self.assertIn('_auth_user_id', self.client.session)
