# Generated by Django 3.2.18 on 2023-11-24 16:57

import django.core.validators
from django.db import migrations, models
import textbooks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('cover', models.ImageField(blank=True, null=True, upload_to=textbooks.models.Textbook.get_cover_path, verbose_name='Обложка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('authors', models.TextField(verbose_name='Авторы')),
                ('pages', models.IntegerField(verbose_name='Количество страниц')),
                ('document', models.FileField(blank=True, null=True, upload_to=textbooks.models.Textbook.get_document_path, verbose_name='Документ')),
                ('rate', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(5.0)], verbose_name='Средняя оценка учебника')),
                ('comments', models.IntegerField(default=0, verbose_name='Количество комментариев')),
            ],
            options={
                'verbose_name': 'Учебник',
                'verbose_name_plural': 'Учебники',
            },
        ),
    ]