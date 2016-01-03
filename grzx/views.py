from django.shortcuts import render
from .models import UserInfo


def index(request):
    userinfo = UserInfo.objects.first()
    return render(request, 'index.html')


def lists(request):
    return render(request, 'list.html')


def news(request):
    return render(request, 'news.html')


def view(request):
    return render(request, 'view.html')