from rest_framework import serializers
from django.db import transaction

from .models import Artist

from utils.images import crop_image

class ArtistPublicSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=1)

    profile_image = serializers.ImageField(required=False, allow_null=True)
    cover_image = serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model = Artist
        fields = [
            "name",
            "bio",
            "profile_image",
            "cover_image",
            "public_id",
        ]
        read_only_fields = ["public_id"]
    
    @transaction.atomic
    def update(self, instance, validated_data):
        pfp_image = validated_data.pop("profile_image", None)
        banner = validated_data.pop("cover_image", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if pfp_image:
            processed = crop_image(pfp_image, 512, 512)
            instance.profile_image.save(processed.name, processed, save=False)

        if banner:
            processed = crop_image(banner, 2560, 1140)
            instance.cover_image.save(processed.name, processed, save=False)

        instance.save()
        return instance


class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=1)

    class Meta:
        model = Artist
        fields = [
            "name",
            "public_id",
        ]
        read_only_fields = ["public_id"]

    @transaction.atomic
    def create(self, validated_data):
        instance = Artist.objects.create(**validated_data)

        return instance