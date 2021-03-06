from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from news.models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'user', 'watch_users', 'created_at', 'updated_at')


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75"')

    get_photo.short_description = 'Photo'

admin.site.register(News)
admin.site.register(Category)