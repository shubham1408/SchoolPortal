# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-11 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenDen', '0004_auto_20200111_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='classroom',
        ),
        migrations.AddField(
            model_name='classrooms',
            name='subject',
            field=models.ManyToManyField(blank=True, to='lenDen.Subjects'),
        ),
    ]
