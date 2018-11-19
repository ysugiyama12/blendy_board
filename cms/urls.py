from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 書籍
    path('post/', views.post_list, name='post_list'),   # 一覧
    path('post/add/', views.post_edit, name='post_add'),  # 登録
    path('post/mod/<int:post_id>/', views.post_edit, name='post_mod'),  # 修正
    path('post/del/<int:post_id>/', views.post_del, name='post_del'),   # 削除
]