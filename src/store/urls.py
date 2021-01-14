from django.urls import path
from .views import (
    about,
    PhotoListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView,
    AllUserPostsView,
    add_to_cart,
    CartItemsView,
    remove_from_cart,
    cart_purchase,
    PhotoFeaturedView,
    check_owned_items,
)

urlpatterns = [
    path('', PhotoListView.as_view(), name='store-home'),
    path('featured/', PhotoFeaturedView.as_view(), name='store-featured'),
    path('user/<str:username>/', AllUserPostsView.as_view(), name='user-photos'),
    path('about/', about, name='about-page'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo-details'),
    path('photo/<int:pk>/add-to-cart/', add_to_cart, name='photo-add-to-cart'),
    path('profile/<str:username>/cart/remove/<int:pk>/', remove_from_cart, name='remove-from-cart'),
    path('profile/<str:username>/cart/', CartItemsView.as_view(), name='cart-view'),
    path('profile/<str:username>/cart/purchase/', cart_purchase, name='purchase'),
    #pk = primary key (ie. the id of each post)
    path('photo/new', PhotoCreateView.as_view(), name='photo-create'),
    #expected name for the template is model_form.html
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo-update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'), #will ask for a confirmation form (template -> photo_confirm_delete
    path('photo/<str:username>/owned_photos/', check_owned_items, name='owned-items')
]