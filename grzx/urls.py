from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lists/', views.lists, name='list'),
    url(r'^news/', views.news, name='news'),
    url(r'^article/(?P<blog_body_id>\d+)/$', views.article, name='article'),
    url(r'^Python/', views.python, name='python'),
    url(r'^abouttest/', views.abouttest, name='abouttest'),
    url(r'^mytalk/', views.mytalk, name='mytalk'),
    url(r'^diary/', views.diary, name='diary'),
    url(r'^add_article/', views.add_article, name='add_article'),
    url(r'^sub_article/', views.sub_article, name='sub_article'),
    url(r'^del_article/(?P<blog_body_id>\d+)/$', views.del_article, name='del_article'),
]
