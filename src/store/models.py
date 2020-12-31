from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image, ImageFile
from django.conf import settings
from django.core.files.base import ContentFile
from io import BytesIO
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True

# Create your models here.
class Photo(models.Model):
    title           = models.CharField(max_length=100)
    pic             = models.ImageField(blank=True, upload_to='')
    thumbnail       = models.ImageField(blank=True, upload_to="thumbnails")
    price           = models.DecimalField(max_digits=1000, decimal_places=2, default=0.01)
    description     = models.TextField(max_length=2500)
    available       = models.BooleanField(default=True)
    featured        = models.BooleanField(default=False)
    date_posted     = models.DateTimeField(default = timezone.now)
    author          = models.ForeignKey(User, on_delete = models.CASCADE)

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
    def save(self, *args, **kwargs): #overriding the save function in order to rescale images (save space, etc.)
        super().save()

        th  = Image.open(self.pic.path)
        th.thumbnail((300,300))

        #if th.height > 300 or th.width > 300:
        #    th.thumbnail((300,300))

        blob = BytesIO()
        th.save(blob, 'JPEG')  
        self.thumbnail.save(str(self.pic), ContentFile(blob.getvalue()), save=False) 
        
        print(self.thumbnail)

        super(Photo, self).save(*args, **kwargs)