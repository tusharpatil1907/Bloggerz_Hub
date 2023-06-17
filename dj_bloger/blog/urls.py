# from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
                path('', home),
                path("blog/<slug:url>",post, name='posts'),
                path("category/<slug:url>",catbypost),
                path("about/",About,name= 'about'),
                ]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)