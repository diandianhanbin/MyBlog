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


def view(request):
    return render(request, 'view.html')