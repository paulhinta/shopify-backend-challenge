from django.db import models

# Create your models here.
class Cart(models.Model):
    products    = []
    full        = models.BooleanField(default=False)
    if len(products) >= 50:
        full = True
    total       = models.DecimalField(max_digits=10000, decimal_places=2, default=0.00)