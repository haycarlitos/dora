import datetime
from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    def __str__(self):
        return self.name

class License(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='licenses'
    )
    license_id = models.CharField(max_length=255)
    license_type = models.CharField(max_length=255)
    package_name = models.CharField(max_length=255)
    expiration_date = models.DateField()

    def __str__(self):
        return self.package_name

    def is_expired(self):

        if self.expiration_date > datetime.datetime.now(timezone.utc):
            return False
        else:
            return True


    


