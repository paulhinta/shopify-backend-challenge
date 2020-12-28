from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name        = models.CharField(max_length=50)
    pic         = models.ImageField(null=True, blank=True)
    featured    = models.BooleanField(default=True)
    description = models.TextField()