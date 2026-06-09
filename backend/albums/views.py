from django.http import JsonResponse, FileResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Album
from .serializers import AlbumSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def album_list(request):
    if request.method == 'GET':
        artist_id = request.GET.get("artist")
        albums = Album.objects.all()

        if artist_id:
            albums = albums.filter(artist__public_id=artist_id)

            serializer = AlbumSerializer(albums, many=True)
            return Response(serializer.data)
            
    if request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)

        if serializer.is_valid():
            album = serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

@api_view(['GET'])
def album_detail(request, pk):
    album = get_object_or_404(Album, public_id=pk)

    serializer = AlbumSerializer(album)

    return Response(serializer.data)

@api_view(['GET'])
def cover_image(request, pk):
    album = get_object_or_404(Album, public_id=pk)

    return FileResponse(album.cover_art.open("rb"))