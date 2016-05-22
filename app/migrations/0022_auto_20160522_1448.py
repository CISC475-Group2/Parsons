# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 19:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 1, 19, 48, 10, 882606, tzinfo=utc), verbose_name='due date'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='evaluates_to',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='test_code',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]