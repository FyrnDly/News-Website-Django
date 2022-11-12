from django.shortcuts import render
from indonesia.models import Post as i
from dunia.models import Post as d
from pendidikan.models import Post as p
from kesehatan.models import Post as k
from teknologi.models import Post as t

# Function Url Path Main Page
def index(request):
    main1 = i.objects.order_by('-time').filter(category='ekonomi')[0]
    main2 = i.objects.order_by('-time').filter(category='pemerintahan')[0]
    main3 = p.objects.order_by('-time')[0]
    main4 = d.objects.order_by('-time')[0]
    post1 = i.objects.order_by('-time')[0:4]
    post2 = d.objects.order_by('-time')[0:4]
    post3 = p.objects.order_by('-time')[0:4]
    post4 = k.objects.order_by('-time')[0:4]
    post5 = t.objects.order_by('-time')[0:4]
    post_list = [post1,post2,post3,post4,post5]
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