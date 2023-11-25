from rest_framework import serializers
from news.models import *
from users.serializers import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class NewReadSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(required=False)
    author = CustomUserSerializer(required=False)
    tag = TagSerializer(required=False)

    class Meta:
        model = New
        fields = ('id', 'cover', 'author', 'content', 'timedate', 'tag')


class NewWriteSerializer(serializers.ModelSerializer):
    cover = serializers.ImageField(required=False)

    class Meta:
        model = New
        fields = ('id', 'cover', 'author', 'content', 'timedate', 'tag')