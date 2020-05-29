from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
# from .views import SignupForm , index
from Postsapp import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'post',views.post, name='index'),
]