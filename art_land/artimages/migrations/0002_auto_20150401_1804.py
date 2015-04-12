# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import artimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('artimages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(to='artimages.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(null=True, upload_to=artimages.models.get_upload_file_name, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
