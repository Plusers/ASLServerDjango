# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-31 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180131_1731'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Add_Books',
            new_name='OperationsWithBooks',
        ),
    ]