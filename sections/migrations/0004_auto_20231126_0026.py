# Generated by Django 3.2.18 on 2023-11-25 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0003_schedule_parlor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='date',
            field=models.DateField(default=datetime.date(2023, 11, 26), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='date',
            field=models.DateField(default=datetime.date(2023, 11, 26), verbose_name='Дата'),
        ),
    ]
