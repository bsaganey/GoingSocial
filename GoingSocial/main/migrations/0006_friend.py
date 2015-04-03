# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150403_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current', models.ForeignKey(related_name='current_user', to='main.MyUser', null=True)),
                ('other', models.ForeignKey(related_name='other_user', to='main.MyUser', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
