from rest_framework import serializers
from video.models import Video,Image


class VideoSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'



class ImageSerializerClass(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
