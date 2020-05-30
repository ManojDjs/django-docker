from django.urls import path, re_path
from .views import chat, room


app_name = 'groupapp'

urlpatterns = [
    path('', chat, name='chat'),
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
