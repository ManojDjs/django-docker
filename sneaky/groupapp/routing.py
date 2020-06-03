# chat/routing.py
from django.urls import re_path,path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer),
]