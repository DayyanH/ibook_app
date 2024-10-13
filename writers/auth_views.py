
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@api_view(['POST'])
def register(request):
    username = request.data.get('name')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': 'Please provide both username and password'}, status=400)
    
    user = User.objects.create_user(username=username, password=password)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=201)

@api_view(['POST'])
def login(request):
    
    username = request.data.get('name')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    
    if not user:
        return Response({'error': 'Invalid credentials'}, status=400)
    
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=200)

@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=204)
