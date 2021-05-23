from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'image')
        extra_kwargs = {'password': {'write_only': True}}


class LoginUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'image',)

