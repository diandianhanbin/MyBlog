# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grzx', '0003_blogbody_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogbody',
            name='blog_clicknum',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogbody',
            name='blog_ismarkdown',
            field=models.CharField(max_length=1, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogbody',
            name='blog_like',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
