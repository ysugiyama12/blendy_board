from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from cms.models import Post
from cms.forms import PostForm

def post_list(request):
    posts = Post.objects.all().order_by('id')
    return render(request, 'cms/post_list.html', {'posts': posts})


def post_edit(request, post_id=None):
    if post_id:   # book_id が指定されている (修正時)
        post = get_object_or_404(Post, pk=post_id)
    else:         # book_id が指定されていない (追加時)
        post = Post()

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            post = form.save(commit=False)
            post.save()
            return redirect('cms:post_list')
    else:    # GET の時
        form = PostForm(instance=post)  # book インスタンスからフォームを作成

    return render(request, 'cms/post_edit.html', dict(form=form, post_id=post_id))


def post_del(request, post_id):
    """書籍の削除"""
    return HttpResponse('書籍の削除')
