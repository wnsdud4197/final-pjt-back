from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('genres/', views.genre_list),
    path('languages/', views.language_list),
]
