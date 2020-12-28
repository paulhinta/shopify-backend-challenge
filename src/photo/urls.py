from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from photo.views import index

print("*********")
print("*********")
print("*********")
print("*********")
print("*********")
print("*********")
print("We are using the URL from src/photo")
print("*********")
print("*********")
print("*********")
print("*********")
print("*********")
print("*********")


urlpatterns = [
    path('', index, name='index'),
]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)