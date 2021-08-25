# yatube/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='index')),
    # path('group/<slug:slug>/', include('posts.urls', namespace='posts')),
]
