# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_hamster_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='likes_cheese',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favorite_art',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='likes_art',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
