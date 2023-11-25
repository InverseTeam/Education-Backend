from rest_framework import serializers
from sections.models import * 
from users.serializers import * 


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'week_day', 'start_time', 'end_time', 'parlor')


class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representative
        fields = ('id', 'firstname', 'lastname', 'surname', 'passport')


class HomeworkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkType
        fields = ('id', 'name')


class HomeworkReadSerializer(serializers.ModelSerializer):
    homework_type = HomeworkTypeSerializer(required=False)

    class Meta:
        model = Homework
        fields = ('id', 'theme', 'homework_type', 'date')


class HomeworkWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ('id', 'theme', 'homework_type', 'date')


class CategorySerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(required=False)

    class Meta:
        model = Category
        fields = ('id', 'cover', 'name')


class GradeReadSerializer(serializers.ModelSerializer):
    student = CustomUserSerializer(required=False)

    class Meta:
        model = Grade
        fields = ('id', 'theme', 'grade', 'date', 'student')


class GradeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id', 'theme', 'grade', 'date', 'student')


class GroupReadSerializer(serializers.ModelSerializer):
    teacher = CustomUserSerializer(required=False)
    students = CustomUserSerializer(required=False, many=True)
    schedules = ScheduleSerializer(required=False, many=True)
    
    class Meta:
        model = Group
        fields = ('id', 'name', 'teacher', 'students', 'schedules', 'total_students', 'max_students')


class GroupWriteSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(required=False, many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'teacher', 'students', 'schedules', 'total_students', 'max_students')

    def create(self, validated_data):
        schedules_data = validated_data.pop('schedules')
        group = Group.objects.create(**validated_data)

        for schedule_data in schedules_data:
            schedule, created = Schedule.objects.get_or_create(**schedule_data)
            group.schedules.add(schedule)

        return group


class SectionReadDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    author = CustomUserSerializer(required=False)
    students = CustomUserSerializer(required=False, many=True)
    grades = GradeReadSerializer(required=False, many=True)
    homeworks = HomeworkReadSerializer(required=False, many=True)
    groups = GroupReadSerializer(required=False, many=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'description', 'category', 'address', 'author', 'students', 'grades', 'homeworks', 'groups', 'rate', 'comments')


class SectionReadListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    author = CustomUserSerializer(required=False)
    groups = GroupReadSerializer(required=False, many=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'description', 'category', 'address', 'author', 'groups', 'rate', 'comments')


class SectionReadHomeworksSerializer(serializers.ModelSerializer):
    homeworks = HomeworkReadSerializer(required=False, many=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'homeworks')


class SectionWriteSerializer(serializers.ModelSerializer):
    groups = GroupWriteSerializer(required=False, many=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'description', 'category', 'address', 'author', 'groups', 'rate', 'comments')

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        section = Section.objects.create(**validated_data)

        for group_data in groups_data:
            group_schedules_data = group_data.pop('schedules', [])
            group = Group.objects.create(**group_data)

            for schedule_data in group_schedules_data:
                schedule, created = Schedule.objects.get_or_create(**schedule_data)
                group.schedules.add(schedule)

            section.groups.add(group)

        return section


class ApplicationReadSerializer(serializers.ModelSerializer):
    student = CustomUserSerializer(required=False)
    section = SectionReadListSerializer(required=False)
    group = GroupReadSerializer(required=False)
    representative = RepresentativeSerializer(required=False)
    document = serializers.FileField(required=False)

    class Meta:
        model = Application
        fields = ('id', 'student', 'section', 'group', 'representative', 'document', 'phone_number', 'approved', 'open')


class ApplicationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'student', 'section', 'group', 'representative', 'document', 'phone_number', 'approved', 'open')