from django.forms import ModelForm, HiddenInput
from cms.models import Post


class PostForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Post
        fields = ('name', 'author', 'content', 'parent')
        widgets = {'parent': HiddenInput}