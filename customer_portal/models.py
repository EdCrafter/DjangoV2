from django.db import models
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from chef_m_portal.models import *


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(13)], max_length = 13)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    chef_m = models.ForeignKey(manager, on_delete=models.PROTECT)
    rent = models.CharField(max_length=8)
    table = models.ForeignKey(tables, on_delete=models.PROTECT)
    days = models.CharField(max_length = 3)
    is_complete = models.BooleanField(default = False)
