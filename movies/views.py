from django.http import response
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db.models import Count

from .serializers import MovieSerializer, GenreSerializer, LanguageSerializer
from .models import Movie, Genre, Language


@api_view(['GET'])
def movie_list(request):
    movie_list = Movie.objects.all()
    serializer = MovieSerializer(movie_list, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def genre_list(request):
    genre_list = Genre.objects.annotate(movie_count=Count('movie')).order_by('-movie_count')
    serializer = GenreSerializer(genre_list, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def language_list(request):
    language_list = Language.objects.annotate(movie_count=Count('movie')).order_by('-movie_count')
    serializer = LanguageSerializer(language_list, many=True)
    return Response(data=serializer.data)