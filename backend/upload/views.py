import django_filters.rest_framework
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Image
from .serializers import ImageUploadSerializer, ImageFilterSerializer


class ImageUploadView(APIView):
    parser_class = (FileUploadParser,)
    serializer_class = ImageUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({}, status=status.HTTP_200_OK)


class ImageFilterView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageFilterSerializer
    filter_fields = ('date', 'size')
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
