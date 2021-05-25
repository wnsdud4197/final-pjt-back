from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('genres/', views.genre_list),
    path('languages/', views.language_list),
    path('movierandom/', views.movie_random),
    path('image/', views.vision_ai),
    path('labels/', views.vision_movie_list),
    path('like/', views.like),
    path('keep/', views.keep),
]