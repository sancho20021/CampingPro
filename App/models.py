from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.IntegerField
    keeper = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
