# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20150405_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about_you',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile_no',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
