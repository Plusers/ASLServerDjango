# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-31 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20190123_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='options',
            field=models.CharField(blank=True, choices=[(1, 'Учебник'), (2, 'Художественная литература')], max_length=100),
        ),
    ]