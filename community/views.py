from django.shortcuts import get_object_or_404
from movies.serializers import MovieSerializer
from movies.models import Movie
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CommunitySerializer, CommunityListSerializer, CommunityDetailSerializer, CommunityUpdateSerializer
from .models import Community

@api_view(['GET', 'POST'])
def community_list(request):
    if request.method == 'POST':
        getmovie = Movie.objects.get(pk=request.data.get('movie'))
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid():
            community = serializer.save(user=request.user, movie=getmovie)
            serializer = CommunityDetailSerializer(community)
            
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'GET':
        community = Community.objects.all()[::-1]
        serializer = CommunityListSerializer(community, many=True)
        return Response(data=serializer.data)
    

@api_view(['POST'])
def detail(request):
    movie_id = request.data.get('id')
    articles = Community.objects.filter(movie_id=movie_id)
    serializer = CommunityDetailSerializer(articles, many=True)
    return Response(data=serializer.data)


@api_view(['PUT', 'DELETE'])
def community_detail(request, article_id):
    article = get_object_or_404(Community, id=article_id)

    if request.method == 'PUT':
        serializer = CommunityUpdateSerializer(
            data=request.data, instance=article
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)