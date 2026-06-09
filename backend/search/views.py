from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q

from artists.models import Artist
from albums.models import Album
from songs.models import Song

from artists.serializers import ArtistSerializer
from albums.serializers import AlbumSerializer
from songs.serializers import SongSerializer


@api_view(['GET'])
def search_view(request):
    q = request.GET.get("q")

    songs = []
    albums = []
    artists = []

    if q:
        songs = Song.objects.filter(
            Q(name__icontains=q)
        )

        albums = Album.objects.filter(
            Q(name__icontains=q)
        )

        artists = Artist.objects.filter(
            Q(name__icontains=q)
        )

    return Response({
        "q": q,
        "albums": albums,
        "artists": artists,
        "songs": SongSerializer(songs, many=True).data,
        "artists": ArtistSerializer(artists, many=True).data,
        "albums": AlbumSerializer(albums, many=True).data,
    })