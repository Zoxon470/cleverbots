import os

from django.db import models


def content_file_name(instance, filename):
    upload_dir = os.path.join('uploads', instance.place)
    return os.path.join(upload_dir, filename)


class Image(models.Model):
    img = models.ImageField('картинка', upload_to=content_file_name, blank=True, null=False)
    place = models.CharField('путь', max_length=125, blank=True)
    date = models.DateTimeField('дата загрузки', auto_now_add=True)
    size = models.BigIntegerField('размер в килобайтах', blank=True)

    def __str__(self):
        return self.img.name

    def save(self, *args, **kwargs):
        self.size = self.img.file.size
        super(Image, self).save(*args, **kwargs)
