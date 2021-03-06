# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-11 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classrooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seating_capacity', models.SmallIntegerField(default=0)),
                ('web_lecture_support', models.BooleanField(default=False)),
                ('shape', models.PositiveSmallIntegerField(choices=[(1, 'oval'), (2, 'rectangular'), (3, 'canopy'), (4, 'elevated')], default=(2, 'rectangular'))),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lenDen.Classrooms')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('DOJ', models.DateField(auto_now=True)),
                ('standard', models.CharField(blank=True, max_length=5, null=True)),
                ('roll_no', models.SmallIntegerField(blank=True, null=True)),
                ('ranking', models.IntegerField(blank=True, null=True)),
                ('point_of_contact', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chapters', models.CharField(blank=True, max_length=400, null=True)),
                ('total_durations', models.DurationField(blank=True, null=True)),
                ('per_class_duration', models.DurationField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('DOJ', models.DateField(auto_now=True)),
                ('salary', models.CharField(blank=True, max_length=400, null=True)),
                ('subjects', models.ManyToManyField(blank=True, to='lenDen.Subjects')),
            ],
        ),
        migrations.AddField(
            model_name='schools',
            name='students',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lenDen.Students'),
        ),
        migrations.AddField(
            model_name='schools',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='lenDen.Subjects'),
        ),
        migrations.AddField(
            model_name='schools',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lenDen.Teachers'),
        ),
    ]
