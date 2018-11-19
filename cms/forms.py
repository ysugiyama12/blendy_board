from django.forms import ModelForm
from cms.models import Post


class PostForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Post
        fields = ('name', 'author', 'content', )