# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-30 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_auto_20190730_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.CharField(default='hello', max_length=32, verbose_name='urlbieming'),
            preserve_default=False,
        ),
    ]
