from django.urls import path

from .views import home, about

urlpatterns = [
    path('', home, name='store-home'),
    path('/about', about, name='about-page'),
]