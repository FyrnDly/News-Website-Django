from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    mainPost = Post.objects.order_by('-time')[0]
    posts= Post.objects.order_by('-time')[1:]
    contentText = {
        'title' : 'Teknologi',
        'path' : 'wkwkNews',
        'post_main' :mainPost,
        'post_list' : posts
    }
    return render(request, 'post/index.html', contentText)

def post(request, slugContent):
    post = Post.objects.get(slug=slugContent)
    recommendation = Post.objects.order_by('-time')[0:6]
    contentText = {
        'title' : post.title,
        'path' : 'Teknologi',
        'content' : post,
        'post_list' : recommendation,
    }
    return render(request, 'post/post.html', contentText)