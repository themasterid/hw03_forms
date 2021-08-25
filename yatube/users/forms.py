# users/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


# * класс для формы регистрации
# * для работы с SignUp в users/views.py
# * и auth/signup/ в users/urls.py
class CreationForm(UserCreationForm):
    """Класс для формы регистрации на сайте."""
    class Meta(UserCreationForm.Meta):
        # * модель для формы
        model = User
        # * эти поля должны быть видны в форме
        fields = (
            'first_name',
            'last_name',
            'username',
            'email'
        )
