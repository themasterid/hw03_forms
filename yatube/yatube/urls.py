# yatube/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='index')),
    path('about/', include('about.urls', namespace='about')),
    path('', include('about.urls', namespace='about')),
]
