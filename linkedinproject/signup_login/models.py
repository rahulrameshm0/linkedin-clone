from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=120, null=True, unique=True)
    email = models.CharField(max_length=150, null=True, unique=True)
    password = models.CharField(max_length=120)
    confirm_pasword = models.CharField(max_length=120)