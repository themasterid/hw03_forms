
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post

User = get_user_model()


def index(request):
    template = 'posts/index.html'
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    author = User.objects.get(username=username)
    post_list = Post.objects.filter(author=author)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'author': author,
        'post_list': post_list,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    author = User.objects.get(username=post.author)
    posts_cnt = Post.objects.filter(author=author).count()
    context = {
        'post': post,
        'posts_cnt': posts_cnt,
    }
    return render(request, 'posts/post_detail.html', context)


# ! DONE !
# ! Декоратор проверяет залогинен ли user
@login_required
def post_create(request):
    """Создает/редактирует пост на сайте."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            group = form.cleaned_data['group']
            search = Post(
                text=text,
                group=group,
                author=request.user
            )
            search.save()
            return redirect('posts:profile', search.author)
        return render(request, 'posts/create_post.html')
    form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id)
    is_edit = True
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            group = form.cleaned_data['group']
            search = Post(
                text=text,
                group=group,
                author=request.user
            )
            search.save()
            print('*' * 100)
            return redirect('posts:post_detail', post_id)
    print('x' * 100)
    form = PostForm()
    return render(
        request,
        'posts/create_post.html',
        {
            'form': form,
            'post': post,
            'is_edit': is_edit,
        })
