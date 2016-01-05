from django.shortcuts import render
from .models import UserInfo, BlogBody


def index(request):
    userinfo = UserInfo.objects.first()
    blog_body = BlogBody.objects.all()[:6]
    return render(request,
                  'index.html',
                  {'userinfo': userinfo, 'blog_body': blog_body})


def lists(request):
    return render(request, 'python_list.html')


def news(request):
    return render(request, 'news.html')


def article(request, blog_body_id=''):
    blog_content = BlogBody.objects.get(id=blog_body_id)
    return render(request, 'view.html', {'blog_content': blog_content})


def python(request):
    # python_blog = BlogBody.objects.filter(blog_type='Python')
    sql = 'select id, blog_title, blog_type, blog_timestamp, blog_body from grzx_blogbody WHERE blog_type = "Python"'
    python_blog = BlogBody.objects.raw(sql)
    return render(request, 'python_list.html', {'python_blog': python_blog})