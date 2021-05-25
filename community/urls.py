from django.urls import path
from . import views

urlpatterns = [
    # GET, POST
    path('', views.community_list),
    path('detail/', views.detail),
    # GET, PUT, DELETE
    path('<int:article_id>/', views.community_detail),

]
