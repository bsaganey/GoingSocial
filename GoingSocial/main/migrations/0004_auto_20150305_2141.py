# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Hometown',
            new_name='hometown',
        ),
    ]
