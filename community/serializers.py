from django.db.models import fields
from movies.models import Movie
from movies.serializers import MovieSerializer
from accounts.serializers import UserSerializer
from rest_framework import serializers
from .models import Comment, Community

class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ('id', 'title', 'content',)


class CommunityListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    user = UserSerializer()

    class Meta:
        model = Community
        fields = '__all__'


class CommunityDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    user = UserSerializer()

    class Meta:
        model = Community
        fields = '__all__'


class CommunityUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ('title', 'content',)


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content',)