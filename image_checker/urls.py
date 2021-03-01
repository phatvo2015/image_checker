from django.conf.urls import url
from .views import FileView,CheckView

# https://blog.vivekshukla.xyz/uploading-file-using-api-django-rest-framework/
urlpatterns = [
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
    url(r'^check/$', CheckView.as_view(), name='check-file-upload'),
]