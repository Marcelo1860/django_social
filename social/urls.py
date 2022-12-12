from django.urls import path

from social.views import profile
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.feed,name = 'feed'),
    path('profile/',views.profile, name = 'profile'),
    path('register/',views.register,name = 'register'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)