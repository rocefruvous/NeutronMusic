from django.urls import path
from . import views

urlpatterns = [
    path("<uuid:pk>/", views.song_detail),
    path("", views.song_view)
]