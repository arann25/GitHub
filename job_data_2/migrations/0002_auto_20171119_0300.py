# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-19 03:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_data_2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelance',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 19, 3, 0, 10, 929840)),
        ),
        migrations.AlterField(
            model_name='job_detail',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 11, 19, 3, 0, 10, 930922)),
        ),
    ]