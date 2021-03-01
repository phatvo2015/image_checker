from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer, CheckeFileSerializer
from .image_crosscheck import crosscheckPersonDB
from .models import CheckFile

from django.conf import settings


class FileView(APIView):
  def post(self, request, *args, **kwargs):  
    # file_serializer = FileSerializer(data=request.data)
    request.data['file'] = (request.data['name'] ,request.data['file'])
    file_serializer = FileSerializer(data=request.data)    
    if file_serializer.is_valid():
      file_serializer.save()      
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckView(APIView):
  def post(self, request, *args, **kwargs):
    # print(request.data)
    request.data['file'] = (request.data['name'] ,request.data['file'])
    serializer = CheckeFileSerializer(data=request.data)
    # print(request.data)
    if serializer.is_valid():
        serializer.save()
        checkResult = crosscheckPersonDB(settings.BASE_DIR + serializer.data['file'])      
        if checkResult[0] == 'User not found':
          formattedRes=  {
            "msg": 'User not found',
            "found": 'False',
            "stored_user_img": "",
            "score": "0"
          }
          return Response(formattedRes, status=status.HTTP_400_BAD_REQUEST)

        else:
          formattedRes =  {
            "msg": checkResult[0],
            "found": checkResult[1][0],
            "stored_user_img":  checkResult[1][1],
            "score":  checkResult[1][2]
          }          

        return Response(formattedRes, status=status.HTTP_201_CREATED)
    else:    
      return Response(serializer.errors, status=400)    
    

      
        
