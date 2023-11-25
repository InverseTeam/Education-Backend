from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.forms import UserChangeForm, UserCreationForm
from users.models import *


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name',)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name',) 


class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'litera')
    search_fields = ('id', 'number', 'litera')
    list_filter = ('number', 'litera')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name', 'role_type')
    search_fields = ('id', 'role_name', 'role_type')
    list_filter = ('role_name',)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'email', 'firstname', 'lastname', 'surname', 'school', 'school_class', 'role', 'is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'firstname', 'lastname', 'surname', 'school', 'school_class', 'achievements', 'role', 'password')}),
        ('Permissions', {'fields': ('is_superuser',)}),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstname', 'lastname', 'surname', 'school', 'school_class', 'role', 'password1', 'password2'),
        }),)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Achievement, AchievementAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)