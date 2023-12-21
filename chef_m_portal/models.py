from django.db import models
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User


class Area(models.Model):
    date = models.CharField(validators = [MinLengthValidator(6), MaxLengthValidator(6)],max_length = 6,unique=True)
    city = models.CharField(max_length = 20)

class manager(models.Model):
    chef_m = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(13)], max_length = 13)
    area = models.OneToOneField(Area, on_delete=models.PROTECT)
    wallet = models.IntegerField(default = 0)

class tables(models.Model):
    table_name = models.CharField(max_length = 20)
    shape = models.CharField(max_length = 10)
    people = models.ForeignKey(manager, on_delete = models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null = True)
    seats = models.CharField(max_length = 2)
    is_available = models.BooleanField(default = True)
    size = models.CharField(max_length = 100)
