from django.shortcuts import render, redirect
from .models import UserInfo, BlogBody
import time
from django.db import connection
# from markdown import markdown


# 处理首页已经日常的视图,包含首页,列表显示,文章详情,以及各个type页的列表
def index(request):
    userinfo = UserInfo.objects.first()
    blog_body = BlogBody.objects.all()[:6:-1]
    hot_rank = BlogBody.objects.all().order_by('-blog_clicknum')[:5]
    return render(request,
                  'index.html',
                  {'userinfo': userinfo, 'blog_body': blog_body, 'hot_rank': hot_rank})


def lists(request):
    return render(request, 'python_list.html')


def news(request):
    return render(request, 'news.html')


def article(request, blog_body_id=''):
    """
    处理点击事件,并且点击数加一
    """
    blog_content = BlogBody.objects.get(id=blog_body_id)
    num = blog_content.blog_clicknum
    num += 1
    blog_content.blog_clicknum = num
    blog_content.save()
    return render(request, 'view.html', {'blog_content': blog_content})


def python(request):
    python_blog = BlogBody.objects.filter(blog_type='Python')[::-1]
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


# 新增文章时调用add_article跳转新增页面,sub_article则吧新增文章处理后自动跳转到文章内容页详情
def add_article(request):
    return render(request, 'add_article.html')


def sub_article(request):
    cursor = connection.cursor()
    if request.method == 'POST':
        mytype = request.POST['article_type']
        title = request.POST['article_title']
        # body = markdown(request.POST['article_editor'])
        body = request.POST['article_editor']
        markdown = request.POST['article_markdown']
        print(markdown)
        updb = BlogBody(blog_title=title, blog_ismarkdown=markdown, blog_body=body, blog_type=mytype, blog_timestamp=time.strftime("%Y-%m-%d %X", time.localtime()), blog_author='点点寒彬', blog_clicknum=1, blog_like=0)
        updb.save()
        cursor.execute('select max(id) from grzx_blogbody where blog_type = %s ', [mytype])
        new_id = cursor.fetchone()
        return redirect('/grzx/article/' + str(new_id[0]) + '/')


# 处理文章删除和编辑
def del_article(request, blog_body_id):
    BlogBody.objects.get(id=blog_body_id).delete()
    return redirect('/')


def edit_article(request):
    pass
