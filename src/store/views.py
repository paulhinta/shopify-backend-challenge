from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Photo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#allows us to verify that user is logged in before creating or update a post; can't use a decorator on class-based views
from PIL import Image
from members.models import Cart
from django.contrib import messages
from django.http.response import HttpResponseRedirect

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

class AddToCartView(DetailView):
    model = Photo

@login_required
def add_to_cart(request, **kwargs):
    user = request.user
    product_id = kwargs['pk']
    product = Photo.objects.filter(id = product_id).first()
    user_cart = Cart.objects.filter(user = user).first()
    user_cart.items.add(product)
    messages.success(request, f"Item was added to {user.username}'s cart: {product.title}")
    return HttpResponseRedirect(reverse('photo-details', args=[product_id]))
    
class AllUserPostsView(ListView): #class-based view
    model = Photo
    template_name = 'store/user_photos.html'
    context_object_name = 'photos' #this is how it's named in the home.html template
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Photo.objects.filter(author=user).order_by('-date_posted')

class CartItemsView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Cart
    template_name = "store/cart_view.html"
    context_object_name = 'cart'

    def test_func(self):
        kuser = get_object_or_404(User, username = self.kwargs.get('username'))
        if self.request.user == kuser: 
            #checks to make sure that a user can only update their own post
            return True
        return False

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        qs =  Cart.objects.filter(user = user)
        photos_in_cart = []
        for c in qs:
            for item in c.items.all():
                photos_in_cart.append(item)
        return photos_in_cart

def about(request):
    return render(request, 'store/about.html', {})