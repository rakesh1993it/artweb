# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artimages', '0012_auto_20150411_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingarticle',
            name='article',
        ),
        migrations.RemoveField(
            model_name='ratingarticle',
            name='user',
        ),
        migrations.DeleteModel(
            name='RatingArticle',
        ),
        migrations.AddField(
            model_name='article',
            name='ratings',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
