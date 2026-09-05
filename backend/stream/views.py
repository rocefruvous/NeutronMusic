from django.http import JsonResponse, FileResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from songs.models import Song

from django.http import FileResponse
from mimetypes import guess_type

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def stream_view(request, pk):
    song = get_object_or_404(Song, public_id=pk)

    file = song.audio.open("rb")

    response = FileResponse(
        file,
        content_type=guess_type(song.audio.name)[0] or "audio/mpeg",
    )

    response["Content-Disposition"] = "inline"
    response["Accept-Ranges"] = "bytes"

    return response