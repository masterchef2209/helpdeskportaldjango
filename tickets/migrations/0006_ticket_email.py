# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-06-14 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20200614_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
    ]
