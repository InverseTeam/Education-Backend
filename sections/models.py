import uuid
import datetime
from django.db import models
from users.models import *
from django_currentuser.db.models import CurrentUserField
from django.core.validators import MinValueValidator, MaxValueValidator


class Schedule(models.Model):
    week_day = models.IntegerField(verbose_name='День недели')
    start_time = models.TimeField(default=datetime.time(), auto_now=False, auto_now_add=False, verbose_name='Время начала')
    end_time = models.TimeField(default=datetime.time(), auto_now=False, auto_now_add=False, verbose_name='Время конца')
    parlor = models.TextField(blank=True, verbose_name='Кабинет')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class Representative(models.Model):
    firstname = models.CharField(max_length=255, verbose_name='Имя')
    lastname = models.CharField(null=True, max_length=255, blank=True, verbose_name='Фамилия')
    surname = models.CharField(null=True, max_length=255, verbose_name='Отчество')
    passport = models.TextField(verbose_name='Пасспорт')

    class Meta:
        verbose_name = 'Законный представитель'
        verbose_name_plural = 'Законные представители'


class Application(models.Model):
    def get_path(instance, filename):
        extension = filename.split('.')[-1]
        image_uuid = uuid.uuid1().hex

        return f'sections/applications/documents/{image_uuid}.{extension}'

    student = CurrentUserField(verbose_name='Ученик')
    section = models.ForeignKey('Section', on_delete=models.CASCADE, related_name='applications_section', verbose_name='Секция')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='applications_group', verbose_name='Группа')
    representative = models.ForeignKey('Representative', on_delete=models.CASCADE, related_name='applications_representative', verbose_name='Законный представитель')
    document = models.FileField(blank=True, null=True, upload_to=get_path, verbose_name='Документ')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    approved = models.BooleanField(default=False, verbose_name='Подтвеждена')
    open = models.BooleanField(default=True, verbose_name='Открытая')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Category(models.Model):
    def get_path(instance, filename):
        extension = filename.split('.')[-1]
        image_uuid = uuid.uuid1().hex

        return f'sections/categories/covers/{image_uuid}.{extension}'
    
    name = models.CharField(max_length=255, verbose_name='Название')
    cover = models.ImageField(blank=True, null=True, upload_to=get_path, verbose_name='Баннер')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class HomeworkType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип ДЗ'
        verbose_name_plural = 'Типы ДЗ'


class Homework(models.Model):
    theme = models.TextField(verbose_name='Тема')
    homework_type = models.ForeignKey('HomeworkType', on_delete=models.CASCADE, related_name='homeworks_homeworktype', verbose_name='Тип ДЗ')
    date = models.DateField(default=datetime.date.today(), verbose_name='Дата')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Домашняя работа'
        verbose_name_plural = 'Домашние работы'


class Grade(models.Model):
    theme = models.TextField(blank=True, null=True, verbose_name='Тема')
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Оценка')
    date = models.DateField(default=datetime.date.today(), verbose_name='Дата')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='grades_student', verbose_name='Ученик')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='groups_teacher', verbose_name='Преподаватель')
    students = models.ManyToManyField(CustomUser, blank=True, related_name='groups_student', verbose_name='Ученики')
    schedules = models.ManyToManyField('Schedule', blank=True, related_name='groups_schedule', verbose_name='Ячейки расписаний')
    total_students = models.IntegerField(default=0, verbose_name='Всего студентов')
    max_students = models.IntegerField(default=0, verbose_name='Максимально студентов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Section(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='sections_category', verbose_name='Категория')
    address = models.TextField(verbose_name='Адрес')
    author = CurrentUserField(verbose_name='Создатель секции')
    students = models.ManyToManyField(CustomUser, blank=True, related_name='sections_student', verbose_name='Ученики')
    grades = models.ManyToManyField('Grade', blank=True, related_name='sections_grade', verbose_name='Оценки')
    homeworks = models.ManyToManyField('Homework', blank=True, related_name='sections_homework', verbose_name='ДЗ')
    groups = models.ManyToManyField('Group', blank=True, related_name='sections_group', verbose_name='Группы')
    rate = models.FloatField(default=0.0, validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], verbose_name='Средняя оценка секции')
    comments = models.IntegerField(default=0, verbose_name='Комментарии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'