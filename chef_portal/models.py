from django.db import models
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User


class Area(models.Model):
    pincode = models.CharField(validators = [MinLengthValidator(6), MaxLengthValidator(6)],max_length = 6,unique=True)
    city = models.CharField(max_length = 20)

class CarDealer(models.Model):
<<<<<<<< HEAD:chef_m_portal/models.py
    chef_m = models.OneToOneField(User, on_delete=models.CASCADE)
========
    chef = models.OneToOneField(User, on_delete=models.CASCADE)
>>>>>>>> b9cc3765ce8c190e81092c2d031994f7577414ba:chef_portal/models.py
    mobile = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(13)], max_length = 13)
    area = models.OneToOneField(Area, on_delete=models.PROTECT)
    wallet = models.IntegerField(default = 0)

class Vehicles(models.Model):
    table_name = models.CharField(max_length = 20)
    color = models.CharField(max_length = 10)
    dealer = models.ForeignKey(CarDealer, on_delete = models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null = True)
    capacity = models.CharField(max_length = 2)
    is_available = models.BooleanField(default = True)
    description = models.CharField(max_length = 100)