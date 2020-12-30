from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

# Create your models here.
class Profile(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs): #overriding the save function in order to rescale images (save space, etc.)
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            img.thumbnail((300,300))
            img.save(self.image.path)