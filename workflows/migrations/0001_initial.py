# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, unique=True, null=True, blank=True)),
                ('created', models.DateField(default=datetime.date.today)),
                ('tooltip', models.CharField(max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, unique=True, null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(default='', max_length=512)),
                ('views', models.IntegerField(default=0)),
                ('downloads', models.IntegerField(default=0)),
                ('versionInit', models.CharField(max_length=128)),
                ('client_ip', models.GenericIPAddressField()),
                ('keywords', models.CharField(default='', max_length=256)),
                ('json', models.CharField(max_length=128)),
                ('created', models.DateField(default=datetime.date.today)),
                ('category', models.ManyToManyField(to='workflows.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
