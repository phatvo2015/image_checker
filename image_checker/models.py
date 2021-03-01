from django.db import models

# https://blog.vivekshukla.xyz/uploading-file-using-api-django-rest-framework/
class File(models.Model):
  file = models.ImageField(blank=False, null=False, upload_to="static_media")
  name = models.CharField(max_length=255)
  timestamp = models.DateTimeField(auto_now_add=True)


class CheckFile(models.Model):
  file = models.ImageField(blank=False, null=False, upload_to="crosscheck_media")
  name = models.CharField(max_length=255)
  timestamp = models.DateTimeField(auto_now_add=True)  