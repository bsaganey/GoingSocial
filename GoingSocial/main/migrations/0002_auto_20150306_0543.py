# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('name', models.CharField(max_length=200)),
                ('hometown', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=75)),
                ('birth', models.DateField()),
                ('zipcode', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex=b'^\\d{5}(?:[-\\s]\\d{4})?$')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
