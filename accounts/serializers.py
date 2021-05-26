from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.serializers import MovieSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=False, allow_empty_file=True, required=False)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'image')
        extra_kwargs = {'password': {'write_only': True}}


class LoginUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'image',)


class UserKeepLikeSerializer(serializers.ModelSerializer):
    keep_movies = MovieSerializer(many=True, read_only=True)
    like_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('keep_movies', 'like_movies',)


class MovieCheckSerializer(serializers.ModelSerializer):
    keep_check = serializers.BooleanField()
    like_check = serializers.BooleanField()

    class Meta:
        model = User
        fields = ('keep_check', 'like_check',)