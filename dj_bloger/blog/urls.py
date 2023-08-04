# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
                  path('', home, name='home'),
                  path('home/', home),
                path("blog/<slug:url>",post, name='posts'),
                  path('update/<slug:url>', edit, name='edit'),
                  path('validate/<slug:url>', updatefn, name='edit'),
                  path("category/<slug:url>", catbypost, name="catbypost"),
                path("about/",About,name= 'about'),
                  path('signup/', sign__up, name='signup'),
                  path('create_post/', create_post, name='create_post'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
