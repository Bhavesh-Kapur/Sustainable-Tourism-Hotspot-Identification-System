# models.py

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    country = models.CharField(max_length=100)



class location(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    add = models.CharField(max_length=200)
    acti = models.CharField(max_length=1000)
    culture = models.CharField(max_length=100000)

