# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 16:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_auto_20170329_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='crawler_ip',
        ),
    ]