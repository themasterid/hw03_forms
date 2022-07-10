# posts/tests/tests_url.py
from django.contrib.auth import get_user_model
from django.test import Client, TestCase

from ..models import Group, Post

User = get_user_model()


class PostURLTestsAll(TestCase):
    def setUp(self):
        # Создаем неавторизованный клиент
        self.guest_client = Client()

    # Проверяем общедоступные страницы
    def test_index_url_exists_at_desired_location(self):
        """Страница / доступна любому пользователю."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)


class PostURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создадим запись в БД для проверки доступности адреса task/test-slug/
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовая группа',
        )

    def setUp(self):
        # Создаем неавторизованный клиент
        self.guest_client = Client()
        # Создаем пользователя
        self.user = PostURLTests.user
        # Создаем второй клиент
        self.authorized_client = Client()
        # Авторизуем пользователя
        self.authorized_client.force_login(self.user)

    def test_index_url_exists_at_desired_location(self):
        """Страница / доступна любому пользователю."""
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_url_exists_at_desired_location_authorized(self):
        """Страница / доступна любому пользователю."""
        response = self.authorized_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_group_detail_url_exists_at_desired_location_authorized(self):
        """Страница /group/test-slug/ доступна авторизованному
        пользователю."""
        response = self.authorized_client.get('/group/test-slug/')
        self.assertEqual(response.status_code, 200)

    # Проверяем редиректы для неавторизованного пользователя
    def test_group_detail_url_exists_at_desired_location_anonymous(self):
        """Страница /group/test-slug/ доступна для анонимного пользователя."""
        response = self.client.get('/group/test-slug/')
        self.assertEqual(response.status_code, 200)

    # Проверяем редиректы для неавторизованного пользователя
    def test_posts_detail_url_exists_at_desired_location_anonymous(self):
        """Страница /posts/1/ доступна для анонимного пользователя."""
        response = self.client.get('/posts/1/edit/')
        self.assertEqual(response.status_code, 302)

    # Проверяем редиректы для авторизованного пользователя
    def test_posts_detail_url_exists_at_desired_location_authorized(self):
        """Страница /posts/1/edit/ доступна для авторизованного
        пользователя."""
        response = self.authorized_client.get('/posts/1/edit/')
        self.assertEqual(response.status_code, 200)


class StaticURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_homepage(self):
        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_author(self):
        response = self.guest_client.get('/about/author/')
        self.assertEqual(response.status_code, 200)

    def test_tech(self):
        response = self.guest_client.get('/about/tech/')
        self.assertEqual(response.status_code, 200)

    def test_unexisting_page(self):
        response = self.guest_client.get('/unexisting_page/')
        self.assertEqual(response.status_code, 404)
