from django.urls import path
from . import views

urlpatterns = [
    # GET, POST
    path('', views.community_list),
    path('detail/', views.community_detail),
    # GET, PUT, DELETE
    # path('<int:community_id)>', views.community_detail),
]
