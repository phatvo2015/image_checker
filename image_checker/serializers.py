from rest_framework import serializers
# from drf_extra_fields.fields import Base64ImageField
from .models import File,CheckFile

# from digits_operators_recognizer.resolver.models import Image
from rest_framework import serializers

from django.core.files.base import ContentFile
import base64
import six
import uuid
import imghdr

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        print(data)
        fileName, data = data[0],data[1]
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
            	# Break out the header from the base64 content
            	header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
            	decoded_file = base64.b64decode(data)
            except TypeError:
            	self.fail('invalid_image')

            # Generate file name:
            file_name = fileName #str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):

    	extension = imghdr.what(file_name, decoded_file)
    	extension = "jpg" if extension == "jpeg" else extension

    	return extension


# https://blog.vivekshukla.xyz/uploading-file-using-api-django-rest-framework/
class FileSerializer(serializers.ModelSerializer):
  file=Base64ImageField()

  class Meta():
    model = File
    fields = ('file', 'name', 'timestamp')


class CheckeFileSerializer(serializers.ModelSerializer):
  file=Base64ImageField()

  class Meta:
    model=CheckFile
    fields= ('file', 'name', 'timestamp')

