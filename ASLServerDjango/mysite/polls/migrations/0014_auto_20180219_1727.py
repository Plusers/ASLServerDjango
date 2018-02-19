# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-19 17:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20180215_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='borrower',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Выдать книгу'),
        ),
    ]