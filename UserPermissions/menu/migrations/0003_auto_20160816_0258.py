# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-16 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menus_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menus',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]