from django.shortcuts import render, redirect, get_object_or_404
from .models import Post




def post_list(request):
  posts = Post.objects.all().order_by("-id")
  # latest_post = Post.objects.all()[: 4]
  context = {
    "posts" : posts,
  }
  return render(request, "blog/blog.html", context)


def post_detail(request, slug, pk):
  post = get_object_or_404(Post, slug=slug, pk=pk)
  context = {
    "post" : post
  }
  return render(request, "blog/post_detail.html", context)