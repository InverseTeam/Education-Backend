from rest_framework import serializers
from textbooks.models import Textbook


class TextbookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textbook
        fields = ('id', 'name', 'cover', 'description', 'authors', 'pages', 'document', 'rate', 'comments')


class TextbookReadDetailSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(required=False)
    document = serializers.FileField(required=False)

    class Meta:
        model = Textbook
        fields = ('id', 'name', 'cover', 'description', 'authors', 'pages', 'document', 'rate', 'comments')


class TextbookReadListSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(required=False)

    class Meta:
        model = Textbook
        fields = ('id', 'name', 'cover', 'description', 'authors', 'pages', 'rate', 'comments')