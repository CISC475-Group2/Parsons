# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 00:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160411_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='section',
            new_name='classroom',
        ),
        migrations.AddField(
            model_name='section',
            name='lab',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solved',
            name='solved_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 12, 0, 30, 57, 424682, tzinfo=utc), verbose_name='solved time'),
        ),
    ]
