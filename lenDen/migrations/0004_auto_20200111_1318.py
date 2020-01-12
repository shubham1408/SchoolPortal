# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-11 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenDen', '0003_subjects_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='classrooms',
            name='name',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='subjects',
            name='classroom',
            field=models.ManyToManyField(blank=True, to='lenDen.Classrooms'),
        ),
    ]
