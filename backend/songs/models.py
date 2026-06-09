import uuid
from django.db import models

class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid7, editable=False)
    public_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, null=False, unique=True)
    name = models.CharField(max_length=250)
    audio = models.FileField(upload_to="songs/", null=True, blank=True)
    explicit = models.BooleanField(default=False)
    album = models.ForeignKey('albums.Album', on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField()

    class Meta:
        indexes = [
            models.Index(fields=["album", "track_number"]),
        ]