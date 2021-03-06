# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-12 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('schoolid', models.IntegerField()),
                ('state', models.IntegerField()),
                ('activity', models.IntegerField()),
                ('content', models.CharField(max_length=500)),
                ('qq', models.CharField(max_length=15)),
                ('wechat', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('topic', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'communication',
            },
        ),
    ]
