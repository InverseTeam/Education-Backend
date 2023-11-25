from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_currentuser.db.models import CurrentUserField


class Achievement(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название') 

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class School(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    classes = models.ManyToManyField('Class', related_name='schools_class', verbose_name='Классы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'


class Class(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)], verbose_name='Цифра')
    litera = models.CharField(max_length=2, verbose_name='Литера')

    def __str__(self):
        return f'{self.number}{self.litera}'

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Role(models.Model):
    role_name = models.CharField(max_length=60, verbose_name='Название')
    role_type = models.CharField(max_length=100, verbose_name='Тип роли')

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        # if extra_fields['role']: user.role = extra_fields['role']

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    firstname = models.CharField(null=True, max_length=255, blank=True, verbose_name='Имя')
    lastname = models.CharField(null=True, max_length=255, blank=True, verbose_name='Фамилия')
    surname = models.CharField(null=True, max_length=255, verbose_name='Отчество')
    achievements = models.ManyToManyField('Achievement',  blank=True, related_name='users_achievemnt', verbose_name='Достижения')
    school = models.ForeignKey('School', null=True, on_delete=models.CASCADE, related_name='users_school', verbose_name='Школа')
    school_class = models.ForeignKey('Class', null=True, on_delete=models.CASCADE, related_name='users_class', verbose_name='Класс')
    role = models.ForeignKey('Role', null=True, on_delete=models.CASCADE, related_name='users_role', verbose_name='Роль')
    password = models.CharField(max_length=255, verbose_name='Пароль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
