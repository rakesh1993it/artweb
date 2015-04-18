# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artimages', '0008_auto_20150406_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='score',
            field=models.FloatField(default=0, max_length=1),
            preserve_default=True,
        ),
    ]
