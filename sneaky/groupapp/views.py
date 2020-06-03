from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import Room,Message
def chat(request):
    return render(request, 'chat.html', {})
def room(request,room_name):
    print(room_name)
    return render(request, 'chatroom.html', {
        'room_name': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })
