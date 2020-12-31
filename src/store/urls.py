from django.urls import path
from .views import about, PhotoListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView, AllUserPostsView

urlpatterns = [
    path('', PhotoListView.as_view(), name='store-home'),
    path('user/<str:username>/', AllUserPostsView.as_view(), name='user-photos'),
    path('about/', about, name='about-page'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo-details'),
    #pk = primary key (ie. the id of each post)
    path('photo/new', PhotoCreateView.as_view(), name='photo-create'),
    #expected name for the template is model_form.html
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo-update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'), #will ask for a confirmation form (template -> photo_confirm_delete
]