from django.db import models

# Create your models here.
class User(models.Model):
    username        = models.CharField(max_length=50)
    password        = models.CharField(max_length=30)
    vendor          = models.BooleanField(blank=False)
    profilepic      = models.ImageField(blank=True)
    inbox           = {}
    cart            = []
    selling         = []
    if vendor == False:
        selling = None