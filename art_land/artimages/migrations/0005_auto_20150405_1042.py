# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import artimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('artimages', '0004_auto_20150401_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='picture',
        ),
        migrations.AddField(
            model_name='article',
            name='thumnail',
            field=models.FileField(null=True, upload_to=artimages.models.get_upload_file_name, blank=True),
            preserve_default=True,
        ),
    ]
