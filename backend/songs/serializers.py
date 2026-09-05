from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Song
from albums.models import Album
from albums.serializers import AlbumSerializer


class SongSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=1)
    audio = serializers.FileField()

    track_number = serializers.IntegerField(required=True)

    album = serializers.SlugRelatedField(
        slug_field="public_id",
        queryset=Album.objects.all(),
        write_only=True
    )

    album_details = AlbumSerializer(
        source="album",
        read_only=True
    )

    class Meta:
        model = Song
        fields = [
            "public_id",
            "name",
            "album",
            "album_details",
            "track_number",
            "explicit",
            "audio",
        ]

        read_only_fields = [
            "public_id",
        ]

        validators = [
            UniqueTogetherValidator(
                queryset=Song.objects.all(),
                fields=["album", "track_number"]
            )
        ]

    @transaction.atomic
    def create(self, validated_data):
        return Song.objects.create(**validated_data)