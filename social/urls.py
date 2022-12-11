from django.urls import path

from social.views import profile
from . import views

urlpatterns = [
    path('', views.feed,name = 'feed'),
    path('profile/',views.profile, name = 'profile'),
]