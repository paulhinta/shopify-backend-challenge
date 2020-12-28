from django.shortcuts import render

# Create your views here.
import os
from django.conf import settings
from django.templatetags.static import static

def index(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/images')
    context = {'images' : img_list}
    return render(request, "photo/index.html", context)