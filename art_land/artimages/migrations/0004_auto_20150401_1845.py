# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artimages', '0003_auto_20150401_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created',
        ),
        migrations.RemoveField(
            model_name='article',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='modified',
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date_published'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'date_published'),
            preserve_default=True,
        ),
    ]
