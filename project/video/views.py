from django.shortcuts import render
from video.serializer import VideoSerializerClass,ImageSerializerClass
from video.models import Video,Image
from rest_framework.viewsets import  ModelViewSet
# Create your views here.





class VideoAPIView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializerClass



class ImageAPIView(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializerClass