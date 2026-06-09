from django.http import JsonResponse, FileResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status


from .models import Artist
from .serializers import ArtistSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def artist_list(request):
    if request.method == 'GET':
            serializer = ArtistSerializer(Artist.objects.all()[:100], many=True)
            return Response(serializer.data)
            
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid():
            artist = serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


@api_view(['GET'])
def artist_detail(request, pk):
    artist = get_object_or_404(Artist, public_id=pk)

    serializer = ArtistSerializer(artist)

    return Response(serializer.data)

@api_view(['GET'])
def profile_image(request, pk):
    artist = get_object_or_404(Artist, public_id=pk)

    return FileResponse(artist.profile_image.open("rb"))

@api_view(['GET'])
def cover_image(request, pk):
    artist = get_object_or_404(Artist, public_id=pk)

    return FileResponse(artist.cover_image.open("rb"))