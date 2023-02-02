from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()

class License(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='licenses'
    )
    license_id = models.CharField(max_length=255)
    license_type = models.CharField(max_length=255)
    package_name = models.CharField(max_length=255)
    expiration_date = models.DateField()