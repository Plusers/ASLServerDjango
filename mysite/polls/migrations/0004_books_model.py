# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-08 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190104_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('clas', models.CharField(max_length=200, verbose_name='Класс')),
                ('num_izd', models.CharField(max_length=200, verbose_name='Номер издания')),
                ('name_izd', models.CharField(max_length=200, verbose_name='Название издания')),
                ('quantity', models.IntegerField(verbose_name='Количество книг')),
                ('status', models.IntegerField(default=0, verbose_name='Выдана книга(1) или нет(0)')),
                ('qr_code', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]