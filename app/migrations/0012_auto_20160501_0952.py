# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 14:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160429_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='compiles_to',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 11, 14, 52, 54, 681496, tzinfo=utc), verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='solution',
            field=models.TextField(default=''),
        ),
    ]