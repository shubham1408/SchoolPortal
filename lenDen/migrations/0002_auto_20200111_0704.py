# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-11 07:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lenDen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='classrooms',
            table='classrooms',
        ),
        migrations.AlterModelTable(
            name='schools',
            table='schools',
        ),
        migrations.AlterModelTable(
            name='students',
            table='students',
        ),
        migrations.AlterModelTable(
            name='subjects',
            table='subjects',
        ),
        migrations.AlterModelTable(
            name='teachers',
            table='teachers',
        ),
    ]