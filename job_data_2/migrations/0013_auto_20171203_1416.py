# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 14:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_data_2', '0012_auto_20171203_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labor_gov',
            name='working_day_number_float',
        ),
        migrations.RemoveField(
            model_name='labor_gov',
            name='working_hours_number_float',
        ),
        migrations.AlterField(
            model_name='freelance',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 12, 3, 14, 16, 19, 662860)),
        ),
        migrations.AlterField(
            model_name='job_detail',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 12, 3, 14, 16, 19, 664084)),
        ),
    ]
