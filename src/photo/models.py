from django.db import models

# Create your models here.
class Photo(models.Model):
    name        = models.CharField(max_length=50)
    content     = models.ImageField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2, default=0.01)
    description = models.TextField()
    owner       = models.CharField(max_length=100)
    copies_sold = models.IntegerField(default=0)

