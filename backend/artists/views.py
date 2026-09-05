import os

from django.conf import settings
from django.http import JsonResponse, FileResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Artist
from .serializers import ArtistSerializer, ArtistPublicSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def artist_list(request):
    if request.method == 'GET':
            serializer = ArtistPublicSerializer(Artist.objects.all()[:100], many=True)
            return Response(serializer.data)
            
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid():
            artist = serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


@api_view(['GET', 'PATCH'])
def artist_detail(request, pk):
    artist = get_object_or_404(Artist, public_id=pk)

    if request.method == 'GET':
        serializer = ArtistPublicSerializer(artist)

        return Response(serializer.data)

    if request.method == 'PATCH':

        serializer = ArtistPublicSerializer(
            artist,
            data=request.data,
            partial=True
    )   

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def profile_image(request, pk):
    artist = get_object_or_404(Artist, public_id=pk)

    if artist.profile_image and os.path.exists(artist.profile_image.path):
        return FileResponse(artist.profile_image.open("rb"))

    fallback_path = os.path.join(settings.BASE_DIR, "static", "images", "default-profile.webp")
    return FileResponse(open(fallback_path, "rb"))

@api_view(['GET'])
def cover_image(request, pk):
    artist = get_object_or_404(Artist, public_id=pk)

    return FileResponse(artist.cover_image.open("rb"))