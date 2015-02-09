# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20150127_1947'),
        ('matches', '0004_auto_20150127_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='game',
            field=models.ForeignKey(default=1, verbose_name='Game', to='community.Game'),
            preserve_default=False,
        ),
    ]
