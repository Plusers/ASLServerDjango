# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-02-05 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_books_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='options',
            field=models.CharField(choices=[(1, 'Учебник'), (2, 'Художественная литература')], max_length=100, verbose_name='Вид книги:'),
        ),
    ]
