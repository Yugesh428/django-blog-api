from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MediaFile
from .serializers import MediaFileSerializer


# Create your views here.
@api_view(['GET','POST'])
def media_list(request):

    if request.method == 'GET':
        files = MediaFile.objects.all()
        serializer = MediaFileSerializer(files,many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = MediaFileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    


@api_view(['GET','PUT','DELETE'])
def media_detail(request,id):
    try:
        media = MediaFile.objects.get(id=id)
    except MediaFile.DoesNotExist:
        return Response({"error":"Not found"}, status = 404)
    
    if request.method == 'GET':
        serializer = MediaFileSerializer(media)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = MediaFileSerializer(media, data= request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    

    if request.method == 'DELETE':
        media.delete()
        return Response({"message":"Deleted successfully"})