from rest_framework import serializers

from .models import Image


class ImageUploadSerializer(serializers.ModelSerializer):
    place = serializers.CharField()
    img = serializers.ImageField()

    class Meta:
        model = Image
        fields = ('place', 'img')


class ImageFilterSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(required=False)
    size = serializers.IntegerField(required=False)
    place = serializers.CharField(required=False)
    path_to_img = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('date', 'size', 'place', 'path_to_img')

    def get_path_to_img(self, obj):
        return obj.img.path
