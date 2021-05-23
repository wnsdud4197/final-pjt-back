from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, LoginUserSerializer
from .models import User


# Create your views here.
@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')
    
    if password != password_confirmation:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    print(request.data)
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(data=serializer.data)


@api_view(['GET'])
def userinfo(request):
    user = User.objects.get(username=request.user)
    serializer = LoginUserSerializer(user)
    return Response(data=serializer.data)

