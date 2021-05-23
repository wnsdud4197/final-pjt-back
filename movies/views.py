from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db.models import Count

from .serializers import MovieSerializer, GenreSerializer, LanguageSerializer
from .models import Movie, Genre, Language


@api_view(['GET'])
def movie_list(request):
    params = request.GET
    if params.get('genre'):
        genre_id = params.get('genre')
        genre = Genre.objects.get(id=genre_id)
        movie_list = genre.movie_set.all()
    elif params.get('language'):
        language_params = params.get('language')
        movie_list = Movie.objects.filter(language_id=language_params)
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