# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-09 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_current_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='reports_period',
            field=models.CharField(max_length=200, null=True),
        ),
    ]