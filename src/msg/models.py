from django.db import models

# Create your models here.
class Message(models.Model):
    origin      = models.CharField(max_length=50)
    sender      = models.CharField(max_length=50)
    subject     = models.CharField(max_length=200)
    content     = models.TextField()