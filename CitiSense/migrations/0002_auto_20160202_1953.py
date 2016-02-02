# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CitiSense', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lat_top', models.FloatField()),
                ('lng_top', models.FloatField()),
                ('lat_bot', models.FloatField()),
                ('lng_bot', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='sensor',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CitiSense.Area'),
        ),
    ]