# posts/urls.py
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/<post_id>/edit/', views.post_edit, name='edit'),
    path('create/', views.post_create, name='create'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    # Главная страница
    path('', views.index, name='index'),
    # Профайл пользователя
    path('profile/<str:username>/', views.profile, name='profile'),
    # Просмотр записи
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
]
