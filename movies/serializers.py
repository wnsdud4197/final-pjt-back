from rest_framework import serializers
from .models import Movie, Genre, Language

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
        fields = ('original_language', 'name', 'movie_count')
