from django.contrib import admin
from textbooks.models import *


class TextbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cover', 'description', 'authors', 'pages', 'document', 'rate', 'comments')
    search_fields = ('id', 'name', 'authors', 'rate')
    list_filter = ('name', 'authors', 'rate')


admin.site.register(Textbook, TextbookAdmin)