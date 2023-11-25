from django.contrib import admin
from sections.models import *


class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'surname', 'passport')
    search_fields = ('id', 'firstname', 'lastname', 'surname')
    list_filter = ('firstname', 'lastname', 'surname')


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'week_day', 'start_time', 'end_time', 'parlor')
    search_fields = ('id', 'week_day')
    list_filter = ('week_day',)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'section', 'group', 'representative', 'phone_number', 'approved', 'open', 'document')
    search_fields = ('id', 'student')
    list_filter = ('student',)
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cover')
    search_fields = ('id', 'name')
    list_filter = ('name',)


class HomeworkTypyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name',)


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'homework_type', 'date')
    search_fields = ('id', 'theme', 'date')
    list_filter = ('theme', 'date')


class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'grade', 'date', 'student')
    search_fields = ('id', 'theme', 'grade')
    list_filter = ('theme', 'grade')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher', 'total_students', 'max_students')
    search_fields = ('id', 'name', 'teacher')
    list_filter = ('name',)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'address', 'author', 'rate', 'comments')
    search_fields = ('id', 'name')
    list_filter = ('name',)


admin.site.register(Representative, RepresentativeAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(HomeworkType, HomeworkTypyAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Section, SectionAdmin)

