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

class Like(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "song"], name="unique_user_song_like")
        ]
        indexes = [
            models.Index(fields=["user", "created_at"]),
            models.Index(fields=["song", "created_at"]),
        ]