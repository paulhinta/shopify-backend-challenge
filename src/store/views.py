from django.shortcuts import render
from .models import Photo

posts = [
    {
        'author'    : 'Paul',
        'title'     : 'My first post',
        'content'   : 'my content',
        'date'      : 'january'
    },
    {
        'author'    : 'Jack',
        'title'     : 'My second post',
        'content'   : 'my content',
        'date'      : 'february'
    },
    {
        'author'    : 'Syndy',
        'title'     : 'My first post',
        'content'   : 'my content',
        'date'      : 'january'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts' : Photo.objects.all(),
        'title' : 'My title',
    }
    return render(request, 'store/home.html', context)
    #can access any key from context within the home.html template

def about(request):
    return render(request, 'store/about.html', {})