# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artimages', '0009_article_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=500)),
                ('Atmcard', models.BooleanField(default=False)),
                ('Mobile_No', models.IntegerField(default=0)),
                ('Cash_on_delevary', models.BooleanField(default=False)),
                ('Date', models.DateTimeField(auto_now_add=True, null=True)),
                ('article', models.ForeignKey(to='artimages.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='article',
            name='score',
        ),
    ]
