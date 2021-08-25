from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # Полный адрес страницы регистрации - auth/signup/,
    # но префикс auth/ обрабатывется в головном urls.py
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path(
        'login/',
        LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),

    # TODO /auth/password_change/
    # TODO /auth/password_change/done/

    # TODO /auth/password_reset/
    # TODO /auth/password_reset/done/ (/auth/reset/done/)

    # TODO password_reset_complete.html
    # TODO password_reset_confirm.html
]
