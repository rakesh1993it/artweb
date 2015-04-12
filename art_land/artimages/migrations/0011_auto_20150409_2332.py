# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artimages', '0010_auto_20150409_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyArticle',
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
            model_name='buyimage',
            name='article',
        ),
        migrations.DeleteModel(
            name='BuyImage',
        ),
    ]
