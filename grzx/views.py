from django.shortcuts import render, redirect
from .models import UserInfo, BlogBody
import time


def index(request):
    userinfo = UserInfo.objects.first()
    blog_body = BlogBody.objects.all()[:6:-1]
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
    python_blog = BlogBody.objects.filter(blog_type='Python')[::-1]
    # sql = 'select id, blog_title, blog_type, blog_timestamp, blog_body from grzx_blogbody WHERE blog_type = "Python"'
    # python_blog = BlogBody.objects.raw(sql)
    return render(request, 'python_list.html', {'python_blog': python_blog})


def abouttest(request):
    test_blog = BlogBody.objects.filter(blog_type='abouttest')[::-1]
    return render(request, 'test_list.html', {'test_blog': test_blog})


def mytalk(request):
    mytalk_blog = BlogBody.objects.filter(blog_type='mytalk')[::-1]
    return render(request, 'mytalk_list.html', {'mytalk_blog': mytalk_blog})


def diary(request):
    diary_blog = BlogBody.objects.filter(blog_type='diary')[::-1]
    return render(request, 'diary_list.html', {'diary_blog': diary_blog})


def add_article(request):
    return render(request, 'add_article.html')


def sub_article(request):
    if request.method == 'GET':
        mytype = request.GET['article_type']
        title = request.GET['article_title']
        body = request.GET['article_editor']
        updb = BlogBody(blog_title=title, blog_body=body, blog_type=mytype, blog_timestamp=time.strftime("%Y-%m-%d %X", time.localtime()), blog_author='点点寒彬')
        updb.save()
        return redirect('/grzx/'+mytype)
