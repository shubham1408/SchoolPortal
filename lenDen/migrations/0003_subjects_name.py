# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-11 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenDen', '0002_auto_20200111_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]