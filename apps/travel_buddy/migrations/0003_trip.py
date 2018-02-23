# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel_buddy', '0002_remove_user_date_hired'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('trave_start_date', models.DateField()),
                ('trave_end_date', models.DateField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('planned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='travel_buddy.User')),
            ],
        ),
    ]
