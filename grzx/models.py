from django.db import models
from django.contrib import admin


class BlogBody(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_body = models.TextField()
    blog_type = models.CharField(max_length=50)
    blog_timestamp = models.DateTimeField()


class UserInfo(models.Model):
    nickname = models.CharField(max_length=20)
    work = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=20)


admin.site.register(BlogBody)
admin.site.register(UserInfo)