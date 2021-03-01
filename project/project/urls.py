from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import image_checker.views

from django.conf import settings
from django.conf.urls.static import static



from django.conf.urls import url
from image_checker.views import FileView,CheckView

urlpatterns = [

    url(r'^upload/$', FileView.as_view(), name='file-upload'),
    url(r'^check/$', CheckView.as_view(), name='check-file'),
    path("admin/", admin.site.urls),    
    
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

