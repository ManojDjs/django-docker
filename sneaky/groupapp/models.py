from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages',on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)