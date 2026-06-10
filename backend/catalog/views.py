from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from artists.models import Artist
from albums.models import Album
from songs.models import Song

from artists.serializers import ArtistSerializer
from albums.serializers import AlbumSerializer
from songs.serializers import SongSerializer

from django.db.models import Count

@api_view(['GET'])
def browse_view(request):
    top_songs = Song.objects.annotate(
        likes_count=Count("like")
    ).order_by("-likes_count")[:10]

    featured_artists = Artist.objects.all()[:10]

    albums = Album.objects.all()[:10]

    recent_albums = Album.objects.order_by(
        "-release_date", "-public_id"
    )[:10]

    return Response({
        "topSongs": SongSerializer(top_songs, many=True).data,
        "featuredArtists": ArtistSerializer(featured_artists, many=True).data,
        "albums": AlbumSerializer(albums, many=True).data,
        "recentAlbums": AlbumSerializer(recent_albums, many=True).data,
    })
