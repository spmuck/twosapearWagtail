# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 02:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160417_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='date',
            field=models.DateField(default=datetime.date(2016, 4, 19)),
        ),
    ]
