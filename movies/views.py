from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db.models import Count
from rest_framework.serializers import Serializer

from .serializers import MovieSerializer, GenreSerializer, LanguageSerializer, VisionSerializer
from .models import Movie, Genre, Language

import os

from google.cloud import vision
from google.cloud.vision_v1 import types

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


@api_view(['GET'])
def movie_random(request):
    movie = Movie.objects.order_by('?')[0]
    print(movie)
    serializer = MovieSerializer(movie)
    print(serializer)
    return Response(data=serializer.data)


@api_view(['POST'])
def vision_ai(request):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './hazel-cipher-314701-3c5c06b3d6d5.json'
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    #set this thumbnail as the url
    image = types.Image()
    # image.source.image_uri = 'https://i.ytimg.com/vi/UQQHSbeIaB0/maxresdefault.jpg'
    image = request.data.get('image')
    
    #### LABEL DETECTION ######
    response_label = client.label_detection(image=image)

    labels = []
    for label in response_label.label_annotations:
        # print({'label': label.description, 'score': label.score})
        labelfor = {}
        labelfor['label'] = label.description
        labelfor['score'] = label.score

        labels.append(labelfor)

    serializer = VisionSerializer(labels, many=True)
    return Response(data=serializer.data)