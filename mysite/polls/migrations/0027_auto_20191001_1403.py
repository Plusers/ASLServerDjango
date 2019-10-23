# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-10-01 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20190810_1120'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BooksGroups',
        ),
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.CharField(max_length=200, null=True, verbose_name='Ссылка на фон новости'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text_of_news',
            field=models.TextField(max_length=1000, null=True, verbose_name='Текст новости'),
        ),
    ]