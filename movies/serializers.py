from django.db.models import fields
from rest_framework import serializers
from .models import Movie, Genre, Language, Vision

class LanguageNameSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="kor_language")
    
    class Meta:
        model = Language
        fields = ('id', 'name',)

class MovieSerializer(serializers.ModelSerializer):
    language = LanguageNameSerializer()

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
    score = serializers.FloatField()
    class Meta:
        model = Vision
        fields = ('label', 'score',)


class VisionListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True)
    class Meta:
        model = Vision
        fields = ('label', 'movie',)

class LikeSerializer(serializers.ModelSerializer):
    check = serializers.BooleanField()

    class Meta:
        model = Movie
        fields = ('check',)