from rest_framework import generics
from news.serializers import *
from rest_framework.permissions import *
from users.permissions import *
from sections.permissions import *


class TagAPIListView(generics.ListAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class NewAPICreateView(generics.CreateAPIView):
    serializer_class = NewWriteSerializer
    permission_classes = [IsAuthenticated, IsTeacher]


class NewAPIListView(generics.ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewReadSerializer
    permission_classes = [IsAuthenticated]