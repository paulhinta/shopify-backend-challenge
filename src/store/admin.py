from django.contrib import admin

# Register your models here.
from .models import Photo, Owners

admin.site.register(Photo)
admin.site.register(Owners)