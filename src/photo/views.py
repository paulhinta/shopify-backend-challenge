from django.shortcuts import render

# Create your views here.
import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static

# Create your views here.
def index(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '\\images')
    context = {'images' : img_list}
    print(context)
    return render(request, "photo/index.html", context)