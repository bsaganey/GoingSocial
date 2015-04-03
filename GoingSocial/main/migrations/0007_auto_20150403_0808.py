# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_friend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='current',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='other',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=3000),
            preserve_default=True,
        ),
    ]
