from django.contrib import admin
from news.models import *


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name',)


class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'timedate', 'cover')
    search_fields = ('id', 'author', 'content')
    list_filter = ('author', 'content')


admin.site.register(Tag, TagAdmin)
admin.site.register(New, NewAdmin)
