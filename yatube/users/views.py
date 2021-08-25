# users/views.py
# Импортируем CreateView, чтобы создать ему наследника
# reverse_lazy позволяет получить URL по параметрам функции path()
# CreationForm импортируем из users/forms.py
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm


class SignUp(CreateView):
    """Класс SignUp создает форму регистрации на сайте."""
    form_class = CreationForm
    # * если регистрация успешная, переходим на главную
    # TODO перепределить на шаблон успешной регистрации?
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'
