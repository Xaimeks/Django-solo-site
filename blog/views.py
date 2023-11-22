from django.shortcuts import render, redirect
from blog.models import Post
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import CommentsForm
from django.urls import reverse
from django.contrib.auth import login



def index(request):
    posts = Post.objects.all()
    posts_per_page = 10
    paginator = Paginator(posts, posts_per_page)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/src/index.html', {'posts': posts})


def about(request):
    return render(request, 'blog/src/about-us.html')


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/src/post_detail.html', {'post': post})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(reverse('post_detail', args=[pk]))


