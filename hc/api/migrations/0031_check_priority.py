# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-21 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20180510_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='priority',
            field=models.CharField(default='normal', max_length=10),
        ),
    ]
