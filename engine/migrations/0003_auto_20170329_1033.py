# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_webpage_crawler_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='crawler_id',
        ),
        migrations.AddField(
            model_name='webpage',
            name='crawler_ip',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
