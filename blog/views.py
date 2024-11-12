from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})
    
from django.http import Http404

def post_detail(request, id, year, month, day, post):
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish_year=year,
                             publish_month=month,
                             publish_day=day)

    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
