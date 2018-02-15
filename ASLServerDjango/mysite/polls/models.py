import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import qrcode

from django.db import models
from django.utils import timezone


class Books(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Название')
    author = models.CharField(blank=False, null=False, max_length=200, verbose_name='Автор')
    clas = models.CharField(blank=False, null=False, max_length=200, verbose_name='Класс')
    numIzd = models.CharField(blank=False, null=False, max_length=200, verbose_name='Номер издания')
    nameIzd = models.CharField(blank=False, null=False, max_length=200, verbose_name='Название издания')
    pub_date = models.DateField('Дата добавления')
    borrower = models.ForeignKey(User,verbose_name='Выдать книгу')
    
    def make_qr_code(self):
        img = qrcode.make(self.name + "/" + self.author + "/" + self.clas +"/"+self.numIzd+"/"+self.nameIzd)
        img.save("/home/vladislav/Документы/ASLServerDjango/ASLServerDjango/qr-books/"self.name+self.author+self.clas+".png")
        img.show()
      
    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

   
    
    def __str__(self):

        return str('Название: {}'.format(self.name)+', Автор: {}'.format(self.author)+', Класс: {}'.format(self.clas)+', Номер издания: {}'.format(self.numIzd)+', Название издания: {}'.format(self.nameIzd))
                

        # return str("Название: "+self.books_name+"/Автор: "+self.books_author+"/Класс: "+self.books_class+"/Номер издания(например 2): "+self.books_numIzd+"/Название издания(например ФГОС): "+self.books_nameIzd)

    def was_published_recently(self):		
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
