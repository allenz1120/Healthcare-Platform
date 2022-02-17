from django.db import models
import uuid

# Create your models here.


class Users(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    pcp = models.CharField(max_length=50)

# class Billing(models.Model):
