from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lists/', views.lists, name='list'),
    url(r'^news/', views.news, name='news'),
    url(r'^view/', views.view, name='view')
]
