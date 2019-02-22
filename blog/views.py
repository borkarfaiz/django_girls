from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    print(posts)
    # posts = get_list_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'posts': posts})


