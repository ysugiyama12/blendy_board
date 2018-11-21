from django.db import models

class Post(models.Model):
    """投稿"""
    name = models.CharField('Title', max_length=255)
    author = models.CharField('Name', max_length=255)
    content = models.TextField('Contents', blank=True)
    parent = models.IntegerField('parent', default=0)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
