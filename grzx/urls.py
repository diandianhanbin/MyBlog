from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lists/', views.lists, name='list'),
    url(r'^news/', views.news, name='news'),
    url(r'^article/(?P<blog_body_id>\d+)/$', views.article, name='article'),
    url(r'^python/', views.python, name='python'),
    url(r'^abouttest/', views.abouttest, name='abouttest'),
]
