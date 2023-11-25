import uuid
from django.db import models
from users.models import *


class Textbook(models.Model):
    def get_cover_path(instance, filename):
        extension = filename.split('.')[-1]
        image_uuid = uuid.uuid1().hex

        return f'textbooks/covers/{image_uuid}.{extension}'
    
    def get_document_path(instance, filename):
        extension = filename.split('.')[-1]
        image_uuid = uuid.uuid1().hex

        return f'textbooks/documents/{image_uuid}.{extension}'
    
    name = models.CharField(max_length=255, verbose_name='Название')
    cover = models.ImageField(blank=True, null=True, upload_to=get_cover_path, verbose_name='Обложка')
    description = models.TextField(verbose_name='Описание')
    authors = models.TextField(verbose_name='Авторы')
    pages = models.IntegerField(verbose_name='Количество страниц')
    document = models.FileField(blank=True, null=True, upload_to=get_document_path, verbose_name='Документ')
    rate = models.FloatField(default=0.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], verbose_name='Средняя оценка учебника')
    comments = models.IntegerField(default=0, verbose_name='Количество комментариев')

    class Meta:
        verbose_name = 'Учебник'
        verbose_name_plural = 'Учебники'