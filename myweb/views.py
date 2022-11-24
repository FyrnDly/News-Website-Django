from django.shortcuts import render
from indonesia.models import Post as i
from dunia.models import Post as d
from pendidikan.models import Post as p
from kesehatan.models import Post as k
from teknologi.models import Post as t

# Function Url Path Main Page
def index(request):
    main1 = k.objects.order_by('-time').filter(category='olahraga')[0]
    main2 = i.objects.order_by('-time').filter(category='pemerintahan')[0]
    main3 = i.objects.order_by('-time').filter(category='ekonomi')[0]
    main4 = d.objects.order_by('-time')[0]
    post_list = []
    post_list.append(i.objects.order_by('-time')[0:3])
    post_list.append(d.objects.order_by('-time')[0:2])
    post_list.append(p.objects.order_by('-time')[0:2])
    post_list.append(k.objects.order_by('-time')[0:2])
    post_list.append(t.objects.order_by('-time')[0:2])
    contentText = {
        'title' : 'Beranda',
        'path' : 'wkwkNews',
        'post1' : main1,
        'post2' : main2,
        'post3' : main3,
        'post4' : main4,
        'posts' :post_list
    }
    return render(request, 'index.html', contentText)

def search(request, search):
    posts = []
    array_post = []
    search = search.replace('-', ' ')
    array_post.append(i.objects.filter(title__icontains=search).order_by('-time'))
    array_post.append(d.objects.filter(title__icontains=search).order_by('-time'))
    array_post.append(k.objects.filter(title__icontains=search).order_by('-time'))
    array_post.append(p.objects.filter(title__icontains=search).order_by('-time'))
    array_post.append(t.objects.filter(title__icontains=search).order_by('-time'))
    
    for list_post in array_post:
        for post in list_post:
            posts.append(post)
    if posts:
        post = posts.pop(0)
    else:
        post = False

    contentText = {
        'posts' : posts,
        'post' : post,
        'title' : 'Pencarian',
        'path' : 'wkwkNews',
        'search' : search,
    }
    return render(request, 'search.html', contentText)
