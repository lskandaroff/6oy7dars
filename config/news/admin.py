from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Type, Flower

# Register your models here.

admin.site.register(Type)


class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'price', 'get_photo')
    list_display_links = ("id", 'name')
    list_editable = ('price',)
    list_filter = ('type',)
    list_per_page = 10

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="150px" >')
        return '-'

admin.site.register(Flower, FlowerAdmin)