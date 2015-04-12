# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artimages', '0006_auto_20150405_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='artimages.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, null=True),
            preserve_default=True,
        ),
    ]
