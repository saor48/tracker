# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-30 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='date_accepted',
            field=models.DateField(blank=True, default=None),
        ),
    ]
