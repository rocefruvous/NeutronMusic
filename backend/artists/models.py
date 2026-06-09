import uuid
from django.db import models

class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid7, editable=False, unique=True)
    public_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, null=False, unique=True)
    name = models.CharField(max_length=250)
    profile_image = models.ImageField(blank=True, null=True, upload_to="artists/profile/")
    cover_image = models.ImageField(blank=True, null=True, upload_to="artists/cover/")
    bio = models.TextField(max_length=1000, blank=True)