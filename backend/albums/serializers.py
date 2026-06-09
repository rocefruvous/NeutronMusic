from rest_framework import serializers
from .models import Album
from artists.models import Artist
from django.db import transaction

from utils.images import crop_image


class AlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=1)
    cover_art = serializers.ImageField(required=False, allow_null=True)

    artist = serializers.SlugRelatedField(
        slug_field="public_id",
        queryset=Artist.objects.all()
    )

    class Meta:
        model = Album
        fields = [
            "name",
            "artist",
            "cover_art",
            "release_date",
            "public_id",
        ]
        read_only_fields = ["public_id"]

    @transaction.atomic
    def create(self, validated_data):
        cover_image = validated_data.pop("cover_art", None)

        instance = Album.objects.create(**validated_data)

        if cover_image:
            try:
                processed = crop_image(cover_image, 512, 512)
            except Exception as exc:
                raise serializers.ValidationError(
                    {"cover_art": str(exc)}
                )

            instance.cover_art.save(
                processed.name,
                processed,
                save=True,
            )

        return instance