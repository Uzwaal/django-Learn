
# from django.urls import path
# from . import views


# urlpatterns=[
#     path('',views.home, name='home'),
#     path('room/',views.room, name='room'),
#     path('furniture/',views.furniture, name='furniture'),
#     path('create-room/', views.createRoom, name='create-room'),
#]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('furniture/', views.furniture, name="furniture"),
    path('room/create/', views.createRoom, name="create-room"),
    path('room/update/<str:pk>/', views.updateRoom, name="update-room"),
]


