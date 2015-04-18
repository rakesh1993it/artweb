# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artimages', '0005_auto_20150405_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='thumnail',
            new_name='picture',
        ),
    ]
