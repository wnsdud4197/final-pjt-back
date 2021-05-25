from movies.serializers import MovieSerializer
from movies.models import Movie
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CommunitySerializer, CommunityListSerializer, CommunityDetailSerializer
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
        community = Community.objects.all()
        serializer = CommunityListSerializer(community, many=True)
        return Response(data=serializer.data)
    
