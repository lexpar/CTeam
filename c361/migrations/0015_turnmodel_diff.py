# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-31 20:12
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('c361', '0014_auto_20160331_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnmodel',
            name='diff',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]
