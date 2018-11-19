from django.db import models

class Post(models.Model):
    """投稿"""
    name = models.CharField('タイトル', max_length=255)
    author = models.CharField('投稿者', max_length=255)
    content = models.CharField('本文', max_length=2000)

    def __str__(self):
        return self.name

# Create your models here.
