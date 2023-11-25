from rest_framework import generics
from textbooks.serializers import *
from rest_framework.permissions import *
from users.permissions import *
from sections.permissions import *


class TextbookAPICreateView(generics.CreateAPIView):
    serializer_class = TextbookWriteSerializer
    permission_classes = [IsAuthenticated, IsTeacher]


class TextbookAPIListView(generics.ListAPIView):
    queryset = Textbook.objects.all()
    serializer_class = TextbookReadListSerializer
    permission_classes = [IsAuthenticated]
