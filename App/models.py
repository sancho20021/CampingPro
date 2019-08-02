from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.IntegerField()
    keeper = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    kol = models.IntegerField(default=0)


class Duty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    keeper = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)


class Text(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()