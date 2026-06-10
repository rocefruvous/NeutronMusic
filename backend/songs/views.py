from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Song, Like
from .serializers import SongSerializer

@api_view(['GET'])
def song_detail(request, pk):
    song = get_object_or_404(Song, public_id=pk)

    serializer = SongSerializer(song)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def song_view(request):
    if request.method == 'GET':
        album_id = request.GET.get("album")
        liked = request.GET.get("liked")
        artist_id = request.GET.get("artist")

        songs = Song.objects.all()

        if artist_id:
            songs = songs.filter(
                album__artist__public_id=artist_id
            )
        if album_id:
            songs = songs.filter(
                album__public_id=album_id
                ).order_by("track_number")

        if liked == "true":
            songs = songs.filter(
                like__user=request.user
            )

        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)

        if serializer.is_valid():
            song = serializer.save()

            return Response(
                SongSerializer(song).data,
                status=201
            )

    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_view(request, pk):
    song = get_object_or_404(Song, public_id=pk)

    like = Like.objects.filter(user=request.user, song=song).first()

    if like:
        like.delete()
        liked = False
    else:
        Like.objects.create(user=request.user, song=song)
        liked = True

    return Response({
        "liked": liked,
        "likes_count": Like.objects.filter(song=song).count()
    }, status=200)