from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list),
    path('<uuid:pk>/', views.album_detail),
    path('<uuid:pk>/cover-image/', views.cover_image),
]