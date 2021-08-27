# posts/forms.py
from django import forms
from django.forms import ModelForm

from .models import Group, Post


class ViewForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group', ]


class PostForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(),
        max_length=400,
        help_text='Текст нового поста',
        label='Текст поста')
    group = forms.ModelChoiceField(
        queryset=Group.objects.select_related(),
        required=False,
        help_text='Группа, к которой будет относиться пост',
        label='Группа')
