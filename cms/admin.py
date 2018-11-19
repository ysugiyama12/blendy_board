from django.contrib import admin
from cms.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'content',)  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目

admin.site.register(Post, PostAdmin)
# Register your models here.
