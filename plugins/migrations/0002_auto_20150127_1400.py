# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        ('plugins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeBoxPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=200, verbose_name='Page Name')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='twitchstreamplugin',
            name='url',
        ),
        migrations.AddField(
            model_name='twitchstreamplugin',
            name='name',
            field=models.CharField(default='tmp', max_length=200, verbose_name='Channel Name'),
            preserve_default=False,
        ),
    ]
