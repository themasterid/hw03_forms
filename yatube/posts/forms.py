# posts/forms.py
from django import forms

from .models import Group, Post

md = ['test1', 'test2']


class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, max_length=400)
    group = forms.ModelChoiceField(
        queryset=Group.objects.select_related(),
        required=False)

    class Meta:
        model = Post


'''
class PostForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('text', 'group')
'''
