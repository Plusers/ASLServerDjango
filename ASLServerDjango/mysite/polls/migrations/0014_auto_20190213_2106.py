# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-02-13 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_remove_userinfo_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='give_date',
            field=models.DateField(default='2019-02-14', verbose_name='Дата выдачи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='pass_date',
            field=models.DateField(default='2019-02-14', verbose_name='Дата сдачи'),
            preserve_default=False,
        ),
    ]
