from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Image


class AdminImage(admin.ModelAdmin):
    list_display = (
        'id',
        'place',
        'date',
        'size',
        'display_image'
    )
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        return mark_safe(
            f'<img src="{obj.img.url}" width="{obj.img.width}" height={obj.img.height} />'
        )


admin.site.register(Image, AdminImage)
