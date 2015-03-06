# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150304_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=200)),
                ('Hometown', models.CharField(max_length=75)),
                ('City', models.CharField(max_length=75)),
                ('birth', models.DateField()),
                ('zipcode', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex=b'^\\d{5}(?:[-\\s]\\d{4})?$')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
