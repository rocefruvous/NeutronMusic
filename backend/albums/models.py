import uuid
from django.db import models

class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid7, editable=False)
    public_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, null=False, unique=True)
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    cover_art = models.FileField(upload_to='album_covers/')
    release_date = models.DateField()