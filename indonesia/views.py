from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    mainPost = Post.objects.order_by('-time')[0]
    posts= Post.objects.order_by('-time')[1:10]
    contentText = {
        'title' : 'Indonesia',
        'path' : 'wkwkNews',
        'post_main' :mainPost,
        'post_list' : posts
    }
    return render(request, 'post/index.html', contentText)

def category(request, category):
    mainPost = Post.objects.filter(category=category)[0]
    posts= Post.objects.filter(category=category)[1:10]
    contentText = {
        'title' : category,
        'path' : 'Indonesia',
        'post_main' :mainPost,
        'post_list' : posts
    }
    return render(request, 'post/index.html', contentText)

def post(request, category,slugContent):
    post = Post.objects.get(slug=slugContent)
    recommendation = Post.objects.filter(category=post.category).order_by('-time')[0:6]
    other = Post.objects.order_by('-time')[0:6]
    contentText = {
        'title' : post.title,
        'path' : f'{post.category.capitalize()} - Indonesia',
        'content' : post,
        'post_list' : recommendation,
        'num_list' : len(recommendation),
        'post_other' :other,
    }
    return render(request, 'post/post.html', contentText)