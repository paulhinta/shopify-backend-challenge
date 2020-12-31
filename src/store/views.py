from django.shortcuts import render
from .models import Photo
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
#allows us to verify that user is logged in before creating a post; can't use a decorator on class-based views

# Create your views here.
def home(request):
    context = {
        'posts' : Photo.objects.all()
    }
    return render(request, 'store/home.html', context)
    #can access any key from context within the home.html template

class PhotoListView(ListView): #class-based view
    model = Photo
    '''
        ListView will look for a template in <app>/<model>_<viewtype>.html
        *** in this case, /store/photo_list.html
        -> instead of creating a new template, just change the template that the listview looks for
    '''
    template_name = 'store/home.html'
    '''
        Still looks for template variable
    '''
    context_object_name = 'photos' #this is how it's named in the home.html template
    ordering = ["-date_posted"] #allows us to post in reverse chronological order

class PhotoDetailView(DetailView):
    model = Photo #Photo is the object that we call the view on

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'pic', 'description', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'store/about.html', {})