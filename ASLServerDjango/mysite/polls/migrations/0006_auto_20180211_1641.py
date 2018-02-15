# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-11 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180204_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.RemoveField(
            model_name='books',
            name='books_author',
        ),
        migrations.RemoveField(
            model_name='books',
            name='books_class',
        ),
        migrations.RemoveField(
            model_name='books',
            name='books_name',
        ),
        migrations.RemoveField(
            model_name='books',
            name='books_nameIzd',
        ),
        migrations.RemoveField(
            model_name='books',
            name='books_numIzd',
        ),
        migrations.AddField(
            model_name='books',
            name='_class',
            field=models.CharField(default=10, max_length=200, verbose_name='Класс'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.CharField(default='author', max_length=200, verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='name',
            field=models.CharField(default='book name', max_length=200, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='nameIzd',
            field=models.CharField(default='1', max_length=200, verbose_name='Название издания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='numIzd',
            field=models.CharField(default='1', max_length=200, verbose_name='Номер издания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='books',
            name='pub_date',
            field=models.DateField(verbose_name='Дата добавления'),
        ),
    ]