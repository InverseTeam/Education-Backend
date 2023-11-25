from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from django.shortcuts import get_object_or_404
from sections.serializers import *
from sections.models import * 
from users.permissions import *
from sections.permissions import *


class SectionAPICreateView(generics.CreateAPIView):
    serializer_class = SectionWriteSerializer
    permission_classes = [IsAuthenticated, IsTeacher]


class SectionAPIListView(generics.ListAPIView):
    serializer_class = SectionReadListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Section.objects.all()
    

class SectionAPILoadListView(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionReadListSerializer
    

class SectionAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionWriteSerializer
    permission_classes = [IsAuthenticated, IsSectionAuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        if self.kwargs['pk']:
            section = Section.objects.get(pk=self.kwargs['pk'])
            serializer = SectionReadDetailSerializer(section)
                
            return Response(serializer.data)
    
        return Response([], status=status.HTTP_404_NOT_FOUND)
    

class GroupAPICreateView(generics.ListAPIView):
    serializer_class = GroupWriteSerializer
    permission_classes = [IsAuthenticated, IsSectionAuthorOrReadOnly]


class ScheduleAPICreateView(generics.CreateAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated, IsSectionAuthorOrTeacherOrReadOnly]

    def post(self, request):
        serializer = ScheduleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            instance = Schedule.objects.get(pk=serializer.data['id'])
            group = Group.objects.get(pk=self.kwargs['pk'])
            group.schedules.add(instance.pk)
            group.save()

            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    

class ApplicationAPICreate(generics.CreateAPIView):
    serializer_class = ApplicationWriteSerializer
    permission_classes = [IsAuthenticated]


class ApplicationAPIMyListView(generics.ListAPIView):
    serializer_class = ApplicationReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(section__author=self.request.user)


class ApplicationAPIConfirmView(generics.UpdateAPIView):
    serializer_class = ApplicationWriteSerializer
    permission_classes = [IsAuthenticated, IsSectionAuthorOrTeacherOrReadOnly]

    def update(self, request, *args, **kwargs):
        obj = get_object_or_404(Application.objects.all(), pk=self.kwargs['pk'])
        section = obj.section
        group = obj.group

        obj.approved = True
        obj.open = False        
        obj.save()
        
        section.students.add(obj.student.id)
        section.save()

        group.students.add(obj.student.id)
        group.save()

        serializer = ApplicationReadSerializer(obj, required=False)

        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
    

class ApplicationAPIRefuseView(generics.UpdateAPIView):
    serializer_class = ApplicationWriteSerializer
    permission_classes = [IsAuthenticated, IsSectionAuthorOrTeacherOrReadOnly]

    def update(self, request, *args, **kwargs):
        obj = get_object_or_404(Application.objects.all(), pk=self.kwargs['pk'])
        obj.open = False
        obj.save()

        serializer = ApplicationReadSerializer(obj, required=False)

        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
    

class HomeworkAPICreateView(generics.CreateAPIView):
    serializer_class = HomeworkWriteSerializer
    permission_classes = [IsAuthenticated, IsSectionAuthorOrTeacherOrReadOnly]

    def post(self, request):
        serializer = GroupWriteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            instance = Homework.objects.get(pk=serializer.data['id'])
            section = Section.objects.get(pk=self.kwargs['pk'])
            section.homeworks.add(instance.pk)
            section.save()

            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    

class HomeworkAPIMyListView(generics.ListAPIView):
    serializer_class = SectionReadHomeworksSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Section.objects.filter(students__in=[self.request.user])


class GradeAPICreateView(generics.CreateAPIView):
    serializer_class = GradeWriteSerializer
    permission_classes = [IsAuthenticated, IsSectionAuthorOrTeacherOrReadOnly]

    def post(self, request):
        serializer = GradeWriteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            instance = Grade.objects.get(pk=serializer.data['id'])
            section = Section.objects.get(pk=self.kwargs['pk'])
            section.grades.add(instance.pk)
            section.save()

            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
    

class GradeAPIMyListView(generics.ListAPIView):
    serializer_class = GradeReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Grade.objects.filter(student=self.request.user) 
    
    
class CategoryAPIListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


