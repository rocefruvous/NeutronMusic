from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid7, editable=False)
    email = models.EmailField(max_length=254, unique=True)
    profile_image = models.ImageField(blank=True, upload_to="profile-images/")
    bio = models.TextField(max_length=254, blank=True)