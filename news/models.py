import uuid
import datetime
from django.db import models
from django_currentuser.db.models import CurrentUserField


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class New(models.Model):
    def get_path(instance, filename):
        extension = filename.split('.')[-1]
        image_uuid = uuid.uuid1().hex

        return f'textbooks/documents/{image_uuid}.{extension}'

    author = CurrentUserField(verbose_name='Автор')
    cover = models.ImageField(blank=True, null=True, upload_to=get_path, verbose_name='Обложка')
    content = models.TextField(verbose_name='Текст')
    timedate = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата оформления')
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='news_tag', verbose_name='Тэг')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
