# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-01 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20181201_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='choice',
        ),
        migrations.AddField(
            model_name='user',
            name='hows_book',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Books', verbose_name='Выдать ученику'),
        ),
    ]
