# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20180220_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='market_type',
            field=models.CharField(choices=[('BSE', '"BSE"'), ('NYM', '"NYM"')], default='BSE', max_length=10),
        ),
    ]
