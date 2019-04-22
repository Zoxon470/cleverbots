import os
from django.db import models


def content_file_name(instance, filename):
    return '/'.join(['content', instance, filename])


class File(models.Model):
    img = models.FileField(upload_to=content_file_name, blank=False, null=False)
    place = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    size = models.BigIntegerField()

    def __str__(self):
        return self.img.name

    def get_file_size(self, value):
        return os.path.getsize(value)
