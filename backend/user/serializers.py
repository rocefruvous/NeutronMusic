from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
import re

from utils.images import crop_image

RESERVED = {"admin", "support", "root", "staff"}

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=3)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]

    def validate_username(self, value):
        value = value.strip().lower()

        if value in RESERVED:
            raise serializers.ValidationError("reserved names not allowed")

        if value[0] in "._-":
            raise serializers.ValidationError("username can't start with symbol")

        if value[-1] in "._-":
            raise serializers.ValidationError("username can't end with symbol")

        if "__" in value or "--" in value:
            raise serializers.ValidationError("repeated symbols not allowed")

        if not re.fullmatch(r"^[a-zA-Z0-9_.-]+$", value):
            raise serializers.ValidationError("invalid characters")

        return value

    def validate_password(self, value):
        try:
            validate_password(value)
        except Exception as e:
            raise serializers.ValidationError(list(e))
        return value

    def validate(self, data):
        password = data.get("password")
        password2 = data.get("password2")

        if not self.instance:
            if not password or not password2:
                raise serializers.ValidationError({"password": "Password fields are required."})

        if password or password2:
            if password != password2:
                raise serializers.ValidationError({"password2": "passwords don't match"})
                
        return data

    def create(self, validated_data):
        validated_data.pop("password2", None)

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"].lower().strip(),
            password=validated_data["password"],
        )

        return user

class PublicUserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False, allow_blank=True)
    profile_image = serializers.ImageField(required=False, allow_null=True)


    def update(self, instance, validated_data):
        image = validated_data.pop("profile_image", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if image:
            processed = crop_image(image, 512, 512)
            instance.profile_image.save(processed.name, processed, save=True)

        return instance

    class Meta:
        model = User
        fields = ["username", "bio", "profile_image", "date_joined"] 