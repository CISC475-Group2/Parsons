# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 23:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160411_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solved',
            name='solved_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 12, 23, 10, 47, 916169, tzinfo=utc), verbose_name='solved time'),
        ),
    ]
