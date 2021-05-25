from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework import serializers
from .models import Community

class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ('id', 'title', 'content',)


class CommunityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = '__all__'

class CommunityDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    
    class Meta:
        model = Community
        fields = '__all__'