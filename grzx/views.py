from django.shortcuts import render
from .models import UserInfo, BlogBody


def index(request):
    userinfo = UserInfo.objects.first()
    blog_body = BlogBody.objects.all()[:6]
    return render(request,
                  'index.html',
                  {'userinfo': userinfo, 'blog_body': blog_body})


def lists(request):
    return render(request, 'list.html')


def news(request):
    return render(request, 'news.html')


def article(request, blog_body_id=''):
    blog_content = BlogBody.objects.get(id=blog_body_id)
    return render(request, 'view.html', {'blog_content': blog_content})