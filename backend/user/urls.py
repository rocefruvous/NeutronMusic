from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
    path('me/', views.me_view),
    path('<str:username>/profile-image/', views.profile_image),
    path('<str:username>/', views.profile_view),
]