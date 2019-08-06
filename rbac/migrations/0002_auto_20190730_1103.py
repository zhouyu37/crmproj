# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-30 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='ROLEandPER'),
        ),
    ]
