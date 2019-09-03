# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-23 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_delete_books_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=200, verbose_name='Предмет'),
        ),
        migrations.AlterField(
            model_name='books',
            name='clas',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='books',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='books',
            name='name_izd',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Название издания'),
        ),
        migrations.AlterField(
            model_name='books',
            name='num_izd',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Номер издания'),
        ),
    ]
