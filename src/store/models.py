from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    title           = models.CharField(max_length=100)
    pic             = models.ImageField(blank=True)
    price           = models.DecimalField(max_digits=1000, decimal_places=2, default=0.01)
    description     = models.TextField(max_length=2500)
    available       = models.BooleanField(default=True)
    featured        = models.BooleanField(default=False)
    date_posted     = models.DateField(default = timezone.now)
    author          = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title