# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-29 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20190726_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(verbose_name='grade(qi)')),
                ('price', models.IntegerField(verbose_name='xuefei')),
                ('start_date', models.DateField(verbose_name='kaipanriqi')),
                ('graduate_date', models.DateField(blank=True, null=True, verbose_name='jieyeriqi')),
                ('memo', models.CharField(blank=True, max_length=255, null=True, verbose_name='shuoming')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='coursename')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='schoolname')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='depart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Depart', verbose_name='departname'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(0, 'man'), (1, 'woman')], verbose_name='xingbie'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Course', verbose_name='kecheng'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.School', verbose_name='xiaoqu'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(related_name='teach_classes', to='crm.User', verbose_name='renkelaoshi'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='crm.User', verbose_name='banzhuren'),
        ),
    ]
