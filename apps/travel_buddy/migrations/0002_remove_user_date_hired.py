# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_hired',
        ),
    ]
