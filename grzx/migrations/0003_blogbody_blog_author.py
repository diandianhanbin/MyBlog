# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grzx', '0002_blogbody_blog_imgurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogbody',
            name='blog_author',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
