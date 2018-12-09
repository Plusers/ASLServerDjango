import datetime
from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import qrcode
from django.urls import reverse

from django.db import models
from django.utils import timezone


class Books(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Название')
    author = models.CharField(blank=False, null=False, max_length=200, verbose_name='Автор')
    clas = models.CharField(blank=False, null=False, max_length=200, verbose_name='Класс')
    num_izd = models.CharField(blank=False, null=False, max_length=200, verbose_name='Номер издания')
    name_izd = models.CharField(blank=False, null=False, max_length=200, verbose_name='Название издания')
    pub_date = models.DateField('Дата добавления')
    quantity = models.IntegerField(blank=False, null=False, verbose_name='Количество книг')
    borrower = models.ForeignKey(User, blank=True, default=None, null=True, verbose_name='Выдать книгу')
    def generate(self):
        filename = "./qr-books/{}.png".format(self.id)
        book_id= str(self.id)
        user = str(self.borrower)
        img_books = qrcode.make("ID: "+book_id+"/ Выдана: "+user)
        img_books.save(filename)
        return filename

    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return 'id:{}, Название:{}, Количество:{}'.format(self.id, self.name,self.quantity)
            
class User(models.Model):
    model = Books
    username = models.CharField(blank=False, null=False, max_length=200, verbose_name='Имя')
    fename = models.CharField(blank=False, null=False, max_length=200, verbose_name='Фамилия')
    third_name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Отчество')
    clas = models.CharField(blank=False, null=False, max_length=200, verbose_name='Класс')
    debt = models.IntegerField(blank=False, null=False, verbose_name='Задолжность')
    hows_book = models.ForeignKey(Books, blank=True, default=None, null=True, verbose_name='Выдать ученику')
    def debt_result(self):
        return str(self.debt)
        
    def getbook(self):
        qwerty = str(self.hows_book)
        return (qwerty)
     
    class Meta():
        verbose_name = "Ученик"
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return 'id:{}, Имя:{}, Фамилия:{}, Отчество:{}, Класс:{} ,Задолжность:{}'.format(self.id, self.username,self.fename,self.third_name,self.clas, self.debt) 

class Place(models.Model):
    name = models.CharField(max_length = 200 )
    keywords = models.CharField(max_length =200)
    