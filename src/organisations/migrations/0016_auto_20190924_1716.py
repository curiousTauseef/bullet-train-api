# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-24 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0015_auto_20190924_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='subscription_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
