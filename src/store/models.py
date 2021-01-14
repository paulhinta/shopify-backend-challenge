from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image, ImageFile
from django.conf import settings
from django.core.files.base import ContentFile
from io import BytesIO
import os
from .watermark import watermark

from django.core.files.storage import default_storage

ImageFile.LOAD_TRUNCATED_IMAGES = True

# Create your models here.
class Photo(models.Model):
    title           = models.CharField(max_length=100)
    pic             = models.ImageField(upload_to='', verbose_name="Upload an image")
    price           = models.DecimalField(max_digits=5, decimal_places=2, default=0.01)
    description     = models.TextField(max_length=2500)
    available       = models.BooleanField(default=True, verbose_name="Leave this box checked to make your Photo available for purchase. You can always change this later.")
    featured        = models.BooleanField(default=False)
    date_posted     = models.DateTimeField(default = timezone.now)
    author          = models.ForeignKey(User, on_delete = models.CASCADE)
    thumbnail       = models.ImageField(blank=True, upload_to="thumbnail")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo-details', kwargs={'pk': self.pk})

    '''
        Get absolute URL allows user to be redirected to the post after creating a new one
        Using reverse > redirect because reverse gives the browser a url as string and browser follows that route
        Redirect does the work itself
        By using reverse, we are letting the view handle the redirect for us instead of the server
    '''

    def get_pic_name(self):
        return str(self.pic)

    def get_price(self):
        return float(self.price)

    def get_id(self):
        return self.pk

    def save(self, *args, **kwargs):
        super().save()

        n = self.get_pic_name()
        watermarked = watermark(n)

        self.thumbnail.save(str(self.pic), ContentFile(watermarked), save=False)

        super(Photo, self).save(*args, **kwargs)

class Owners(models.Model):
    pic    = models.OneToOneField(Photo, on_delete=models.CASCADE)
    owners = models.ManyToManyField(User)

    def get_items(self):
        i = []
        for item in self.owners.all():
            i.append(item)
        return i

    def __str__(self):
        name = str(self.pic) + "'s owners"
        return name