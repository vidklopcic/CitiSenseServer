# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CitiSense', '0002_auto_20160202_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
