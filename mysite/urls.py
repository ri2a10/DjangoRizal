from django.contrib import admin
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("dashboard/", include("blog.urls")),
    path("users/", include("users.urls")),
    path("",index, name="index"),
    path("about/",about, name="about"),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registerasi, name='registerasi'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)