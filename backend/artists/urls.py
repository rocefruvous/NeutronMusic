from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list),
    path('<uuid:pk>/', views.artist_detail),
    path('<uuid:pk>/profile-image/', views.profile_image),
    path('<uuid:pk>/cover-image/', views.cover_image),
]