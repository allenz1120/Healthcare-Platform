from pyexpat import model
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


class Billing(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    insurance_company = models.CharField(max_length=50)
    member_id = models.IntegerField
    member_name = models.CharField(max_length=50)
    credit_card = models.IntegerField
    expiration_date = models.DateField()
    cvv = models.IntegerField
