from django.shortcuts import render, get_object_or_404
from .models import Photo
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#allows us to verify that user is logged in before creating or update a post; can't use a decorator on class-based views
from PIL import Image

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
    paginate_by = 5

class PhotoDetailView(DetailView):
    model = Photo #Photo is the object that we call the view on

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['title', 'pic', 'description', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.thumbnail = None

        return super().form_valid(form)

class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    fields = ['title', 'pic', 'description', 'price']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: 
            #checks to make sure that a user can only update their own post
            return True
        return False

class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo #Photo is the object that we call the view on
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: 
            #checks to make sure that a user can only update their own post
            return True
        return False

class AllUserPostsView(ListView): #class-based view
    model = Photo
    template_name = 'store/user_photos.html'
    context_object_name = 'photos' #this is how it's named in the home.html template
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Photo.objects.filter(author=user).order_by('-date_posted')

def about(request):
    return render(request, 'store/about.html', {})