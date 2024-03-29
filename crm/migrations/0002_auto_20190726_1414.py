# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-26 06:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('gender', models.IntegerField(choices=[(0, 'man'), (1, 'woman')])),
            ],
        ),
        migrations.AlterField(
            model_name='depart',
            name='desc',
            field=models.TextField(verbose_name='depart_desc'),
        ),
        migrations.AlterField(
            model_name='depart',
            name='name',
            field=models.CharField(max_length=32, verbose_name='depart_name'),
        ),
        migrations.AddField(
            model_name='user',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Depart'),
        ),
    ]
