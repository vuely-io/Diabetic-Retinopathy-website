# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diabetics', '0002_auto_20161229_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='severity',
            name='result',
        ),
        migrations.AddField(
            model_name='imagename',
            name='result',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
