# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 03:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160419_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='default_serving_format',
            field=models.CharField(choices=[('quantity', 'Quantity'), ('volume', 'Volume'), ('weight', 'Weight')], default='weight', max_length=10),
        ),
    ]
