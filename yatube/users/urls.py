from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordChangeDoneView,
                                       PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # Полный адрес страницы регистрации - auth/signup/,
    # но префикс auth/ обрабатывется в головном urls.py
    # ! ссылка на форму регистрации пользователя.
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(
        template_name='users/logged_out.html'), name='logout'),
    # ! Ссылка на форму логина пользователя.
    path('login/', LoginView.as_view(
        template_name='users/login.html'), name='login'),
    # ! Ссылка на форму смены пароля.
    path('password_change/', PasswordChangeView.as_view(
        template_name='users/password_change_form.html'),
        name='password_change'),
    # ! Ссылка на страницу подтверждения смены пароля
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'),
        name='password_change_done'),
    # ! Ссылка на страницу подтверждения сброса пароля
    path('password_reset/', PasswordResetView.as_view(
        template_name='users/password_reset_form.html'),
        name='password_reset'),
    # ! Ссылка на страницу подтверждения сброса пароля
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    # ! Ссылка на страницу сброса пароля
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    # ! Ссылка на страницу завершения сброса пароля
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
]
