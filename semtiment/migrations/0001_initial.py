# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semtiment', models.CharField(max_length=4096, null=True)),
                ('view', models.CharField(max_length=4096, null=True)),
                ('sentence', models.TextField(max_length=9999, null=True)),
            ],
        ),
    ]
