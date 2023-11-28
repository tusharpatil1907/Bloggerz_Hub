
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from dj_bloger.blog.views import sign_up

urlpatterns = [
    # path('admin/', admin.site.urls),
                  path('', include('blog.urls')),
                  path('', include('django.contrib.auth.urls')),
                  path('tinymce/', include('tinymce.urls')),

    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
