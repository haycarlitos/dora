import datetime
from django.test import TestCase
from django.utils import timezone
from .models import License


class LicenseModelTests(TestCase):

    def test_is_expired(self):
        """
        is_expired() returns True if the
        license is expired.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = License(expiration_date=time )
        self.assertIs(future_question.is_expired(), False)