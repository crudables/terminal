# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tict', '0003_auto_20170105_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='staff_id',
            field=models.CharField(blank=True, max_length=7, unique=True),
        ),
    ]