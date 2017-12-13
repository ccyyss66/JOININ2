# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-12 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('universityid', models.IntegerField()),
                ('schoolid', models.IntegerField()),
                ('introduce', models.CharField(max_length=500)),
                ('type', models.IntegerField()),
            ],
            options={
                'db_table': 'organize',
            },
        ),
    ]