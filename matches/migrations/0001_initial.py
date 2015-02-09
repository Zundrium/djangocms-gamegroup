# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(verbose_name='Date')),
                ('clanA', models.ForeignKey(related_name='clanA_set', to='community.Clan')),
                ('clanB', models.ForeignKey(related_name='clanB_set', to='community.Clan')),
                ('winner', models.ForeignKey(blank=True, to='community.Clan', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MemberScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kills', models.IntegerField(null=True, verbose_name='Kills', blank=True)),
                ('deaths', models.IntegerField(null=True, verbose_name='Deaths', blank=True)),
                ('assists', models.IntegerField(null=True, verbose_name='Assists', blank=True)),
                ('match', models.ForeignKey(verbose_name='Match', to='matches.Match')),
                ('player', models.ForeignKey(verbose_name='Player', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
