from django.http import JsonResponse, FileResponse

from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status

from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, PublicUserSerializer

User = get_user_model()

@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        return Response("User has been logged in", status=201)
        return redirect('dashboard')
    else:
        return Response("Invalid login", status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response("User has been logged out", status=201)
    

@api_view(['POST'])
def register_view(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        
        return Response({
            "message": "user created",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
@permission_classes([IsAuthenticated])
def me_view(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user)

        return Response(serializer.data)
    if request.method == 'PATCH':
        data = {k: v for k, v in request.data.items() if v != ""}

        serializer = PublicUserSerializer(request.user, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profile_image(request, username):
    user = get_object_or_404(User, username=username)

    return FileResponse(user.profile_image.open("rb"))

@api_view(['GET'])
def profile_view(request, username):
    user = get_object_or_404(User, username=username)

    serializer = PublicUserSerializer(user)

    return Response(serializer.data)