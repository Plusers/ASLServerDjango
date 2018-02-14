# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-12 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20180212_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='givebooks',
            options={'verbose_name': 'Сданная книга', 'verbose_name_plural': 'Сдать книги'},
        ),
        migrations.RenameField(
            model_name='givebooks',
            old_name='clas_of_user',
            new_name='clas_of_users',
        ),
        migrations.AlterField(
            model_name='givebooks',
            name='pub_date',
            field=models.DateField(verbose_name='Дата добавления'),
        ),
    ]
