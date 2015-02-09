# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0003_auto_20150127_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='datetime',
            field=models.DateTimeField(verbose_name='Date'),
            preserve_default=True,
        ),
    ]
