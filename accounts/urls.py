from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('userinfo/', views.userinfo),
    path('user/keep_like/', views.user_keep_like),
    path('movie_check/', views.movie_check),
]
