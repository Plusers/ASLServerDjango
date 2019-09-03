# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-04 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.IntegerField(default=0, verbose_name='Выдана книга(1) или нет(0)'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='debt',
            field=models.IntegerField(blank=True, default=0, verbose_name='Задолжность'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='hows_book',
            field=models.ManyToManyField(blank=True, to='polls.Books', verbose_name='Выдать ученику'),
        ),
    ]
