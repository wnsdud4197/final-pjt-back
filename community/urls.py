from django.urls import path
from . import views

urlpatterns = [
    # GET, POST
    path('', views.community_list),
    path('detail/', views.detail),
    # GET, PUT, DELETE
    path('<int:article_id>/', views.community_detail),
    # GET, POST
    path('<int:article_id>/comments/', views.comments_list),
    # GET, PUT, DELETE
    path('comments/<int:comment_id>/', views.comment_detail),
]
