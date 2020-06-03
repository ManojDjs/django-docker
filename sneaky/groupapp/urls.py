from django.urls import path, re_path
from .views import chat, room,rooms
from django.conf.urls import url

app_name = 'groupapp'

urlpatterns = [
    path('', chat, name='chat'),
    url(r'^group',rooms,name='rooms'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
