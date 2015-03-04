# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contest1',
        ),
        migrations.DeleteModel(
            name='Contest2',
        ),
        migrations.DeleteModel(
            name='Contest3',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
