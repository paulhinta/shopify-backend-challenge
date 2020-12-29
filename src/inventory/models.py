from django.db import models

# Create your models here.
class Inventory(models.Model):
    pics_for_sale   = []
    num_pics        = len(pics_for_sale)