# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0006_auto_20170410_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='url_update',
            field=models.TextField(blank=True, verbose_name='Page URL'),
        ),
    ]
