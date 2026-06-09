from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Song
from albums.models import Album

from mutagen import File as MutagenFile

def get_duration(file_field):
    try:
        audio = MutagenFile(file_field)
        if not audio or not getattr(audio, "info", None):
            return 0
        return int(audio.info.length or 0)
    except Exception:
        return 0

class SongSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=1)
    audio = serializers.FileField()

    track_number = serializers.IntegerField(required=True)
    duration = serializers.IntegerField(read_only=True)

    album = serializers.SlugRelatedField(
        slug_field="public_id",
        queryset=Album.objects.all()
    )

    class Meta:
        model = Song
        fields = [
            "public_id",
            "name",
            "album",
            "track_number",
            "explicit",
            "duration",
            "audio",
        ]

        read_only_fields = [
            "public_id",
            "duration",
        ]

        validators = [
            UniqueTogetherValidator(
                queryset=Song.objects.all(),
                fields=["album", "track_number"]
            )
        ]

    @transaction.atomic
    def create(self, validated_data):
        song = Song.objects.create(**validated_data)

        try:
            song.duration = get_duration(song.audio.file)
        except Exception:
            song.duration = 0

        song.save(update_fields=["duration"])
        return song