# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-29 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_currenttime'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CurrentTime',
        ),
        migrations.AddField(
            model_name='stockpricevariation',
            name='sequence_id',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], default=1),
        ),
    ]