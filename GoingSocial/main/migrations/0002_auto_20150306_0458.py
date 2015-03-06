# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=75)),
                ('name', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=75)),
                ('birth', models.DateField()),
                ('zipcode', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex=b'^\\d{5}(?:[-\\s]\\d{4})?$')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
