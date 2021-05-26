from django.db.models import fields
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework import serializers
from .models import Comment, Community

class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ('id', 'title', 'content',)


class CommunityListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Community
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content', 'user',)

class CommunityDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    comment_set = CommentSerializer(many=True)
    
    class Meta:
        model = Community
        fields = '__all__'


class CommunityUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ('title', 'content',)

