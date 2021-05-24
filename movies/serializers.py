from rest_framework import serializers
from .models import Movie, Genre, Language, Vision

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    movie_count = serializers.IntegerField()

    class Meta:
        model = Genre
        fields = ('id', 'name', 'movie_count')


class LanguageSerializer(serializers.ModelSerializer):
    movie_count = serializers.IntegerField()
    name = serializers.CharField(source="kor_language")
    
    class Meta:
        model = Language
        fields = ('id', 'original_language', 'name', 'movie_count')

class VisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vision
        fields = ('label', 'score',)