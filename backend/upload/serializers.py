from rest_framework import serializers
from .models import File


class FileUploadSerializer(serializers.ModelSerializer):
    place = serializers.CharField(required=True)
    img = serializers.FileField(required=True)

    class Meta:
        model = File
        fields = ('place', 'img')


class FileFilterSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(required=True)
    img = serializers.FileField(required=True)

    class Meta:
        model = File
        fields = ('date', 'img')
