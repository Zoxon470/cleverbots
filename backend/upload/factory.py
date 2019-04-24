import datetime
import factory
from django.conf import settings
from factory.fuzzy import FuzzyInteger
from .models import Image


class ImageFactory(factory.django.DjangoModelFactory):
    img = factory.django.ImageField(color='blue')
    place = f"/app{settings.MEDIA_URL}uploads"
    date = factory.LazyFunction(datetime.datetime.now)
    size = FuzzyInteger(0, 228)

    class Meta:
        model = Image
