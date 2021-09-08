# posts/tests/test_views.py
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from django import forms

from ..models import Group, Post

User = get_user_model()


class TaskPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
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
        self.user = TaskPagesTests.user
        self.post = TaskPagesTests.post
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        templates_pages_names = {
            'posts/index.html': reverse('posts:index'),
            'posts/create_post.html': reverse('posts:create'),
            'posts/group_list.html': reverse(
                'posts:group_list', kwargs={'slug': 'test-slug'}),
            'posts/profile.html': reverse(
                'posts:profile', kwargs={'username': f'{self.user}'}),
            'posts/post_detail.html': reverse(
                'posts:post_detail', kwargs={'post_id': f'{self.post.id}'})
        }

        for template, reverse_name in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    # Проверка словаря контекста главной страницы (в нём передаётся форма)
    def test_home_page_show_correct_context(self):
        """Шаблон home сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse('posts:create'))
        # Словарь ожидаемых типов полей формы:
        # указываем, объектами какого класса должны быть поля формы
        form_fields = {
            'text': forms.fields.CharField,
        }

        # Проверяем, что типы полей формы в словаре
        # context соответствуют ожиданиям
        for value, expected in form_fields.items():
            with self.subTest(value=value):
                form_field = response.context.get('form').fields.get(value)
                # Проверяет, что поле формы является экземпляром
                # указанного класса
                self.assertIsInstance(form_field, expected)

    # Проверяем, что словарь context страницы /task
    # в первом элементе списка object_list содержит ожидаемые значения
    def test_task_list_page_show_correct_context(self):
        """Шаблон task_list сформирован с правильным контекстом."""
        response = self.authorized_client.get(reverse(
            'posts:profile', kwargs={'username': f'{self.user}'}))
        # Взяли первый элемент из списка и проверили, что его содержание
        # совпадает с ожидаемым
        first_object = response.context['page_obj'][0]
        task_text_0 = first_object.text
        self.assertEqual(task_text_0, 'Тестовая группа')

    # Проверяем, что словарь context страницы task/test-slug
    # содержит ожидаемые значения
    def test_task_detail_pages_show_correct_context(self):
        """Шаблон task_detail сформирован с правильным контекстом."""
        response = (
            self.authorized_client.get(
                reverse('posts:group_list', kwargs={'slug': 'test-slug'})))
        self.assertEqual(
            response.context.get('group').title, 'Тестовая группа')
        self.assertEqual(str(response.context.get('group')), 'Тестовая группа')
        self.assertEqual(response.context.get('group').slug, 'test-slug')
