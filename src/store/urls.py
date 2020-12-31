from django.urls import path
from .views import home, about, PhotoListView, PhotoDetailView, PhotoCreateView

urlpatterns = [
    path('', PhotoListView.as_view(), name='store-home'),
    path('about/', about, name='about-page'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo-details'),
    #pk = primary key (ie. the id of each post)
    path('photo/new', PhotoCreateView.as_view(), name='photo-create'),
    #expected name for the template is model_form.html
]