from pyexpat import model
from django.db import models
import uuid
from django.core.validators import int_list_validator

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
    member_id = models.IntegerField()
    member_name = models.CharField(max_length=50)
    credit_card = models.IntegerField()
    expiration_date = models.DateField()
    cvv = models.IntegerField()


class Medical_History(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    family_predisposition = models.CharField(max_length=100)
    allergies = models.CharField(max_length=50)
    medication = models.CharField(max_length=100)
    drinking = models.BooleanField()
    smoking = models.BooleanField()


class Role_Relation(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    rid = models.IntegerField()
    delete = models.BooleanField()
    date_of_change = models.DateField()


class Roles(models.Model):
    rid = models.IntegerField()
    role = models.CharField(max_length=15)

class Device_Blood_Pressure(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    blood_pressure = models.IntegerField()
    last_measured = models.DateField()

class Device_Thermometer(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    last_measured = models.DateField()
