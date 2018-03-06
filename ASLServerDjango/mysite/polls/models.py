import datetime
from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import qrcode

from django.db import models
from django.utils import timezone


class Books(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Название')
    author = models.CharField(blank=False, null=False, max_length=200, verbose_name='Автор')
    clas = models.CharField(blank=False, null=False, max_length=200, verbose_name='Класс')
    num_izd = models.CharField(blank=False, null=False, max_length=200, verbose_name='Номер издания')
    name_izd = models.CharField(blank=False, null=False, max_length=200, verbose_name='Название издания')
    pub_date = models.DateField('Дата добавления')
    borrower = models.ForeignKey(User, blank=True, default=None, null=True, verbose_name='Выдать книгу')

    def generate(self):
        filename = "./qr-books/{}.png".format(self.name)
        book_id= str(self.id)
        img_books = qrcode.make("Название: "+self.name+"/Автор: "+self.author+"/Класс: "+self.clas+"/ID: "+book_id)
        img_books.save(filename)
        return filename

    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return '{}, id:{}'.format(self.name, self.id) 
   