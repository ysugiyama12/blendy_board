from django.db import models

class Post(models.Model):
    """投稿"""
    name = models.CharField('タイトル', max_length=255)
    author = models.CharField('投稿者', max_length=255)
    content = models.TextField('本文', blank=True)
    parent = models.IntegerField('親', default=0)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
