# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='hometown',
            new_name='state',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
    ]
