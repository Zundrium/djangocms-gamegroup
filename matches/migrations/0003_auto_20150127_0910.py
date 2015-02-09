# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_lastmatchesplugin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='datetime',
            field=models.DateTimeField(verbose_name='Datum'),
            preserve_default=True,
        ),
    ]
