# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-20 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c361', '0007_auto_20160314_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameinstancemodel',
            name='world',
            field=models.TextField(blank=True, null=True),
        ),
    ]
