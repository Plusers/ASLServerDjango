import datetime
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import qrcode
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class News(models.Model):
    title = models.CharField(blank=False, null=True, verbose_name='Заголовок новости', max_length=200)
    text_of_news = models.CharField(blank=False, null=True, verbose_name='Текс новости', max_length=200)
    data_pub = models.DateField('Дата публикации новости',null=True)


BOOK=((1,'Учебник'), (2,'Художественная литература'))
class Books(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Наименование')
    author = models.CharField(blank=False, null=False, max_length=200, verbose_name='Предмет')
    clas = models.CharField(blank=True, null=False, max_length=200, verbose_name='Класс',default = '')
    num_izd = models.CharField(blank=True, null=False, max_length=200, verbose_name='Номер издания',default='')
    name_izd = models.CharField(blank=True, null=False, max_length=200, verbose_name='Название издания',default='')
    give_date = models.DateField('Дата выдачи',null=True)
    pass_date = models.DateField('Дата сдачи',null=True)
    type_of_book = models.IntegerField(choices=BOOK, default=1, verbose_name='Вид книги')
    quantity = models.CharField(blank=False, null=False, verbose_name=' ISBN-код', max_length=200)
    #dop_id = models.CharField()
    #qr_code_image = models.ImageField(upload_to='images/', null=False, blank=True)
    status = models.IntegerField(null = False,blank = False, verbose_name='Выдана книга(1) или нет(0)', default=0)
    #options = models.CharField(max_length=100, blank = False, choices=BOOK, verbose_name='Вид книги:')
    #borrower = models.ForeignKey(,blank=True, null=False, verbose_name='Вид книги')
    #qr_code = models.ImageField(upload_to='images/', null=False, blank=True)
    def generate(self):
        filename1 = "./mysite/polls/static/media/images/{}.png".format(self.id)
        filename = "/media/images/{}.png".format(self.id)
        book_id= str(self.id)
        img_books = qrcode.make("ID: "+book_id)
        #img_books.show()
        img_books.save(filename1)
        return filename

    @classmethod
    def create(cls, name,author,clas,num_izd,name_izd):
        book = cls(name=name,author=author,clas = clas,num_izd=num_izd,name_izd = name_izd)
        # do something with the book
        return book

    def change_quantity(self):
        self.quantity-=1
        return self.quantity
    class Meta():
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return 'id:{}, Название:{},Автор:{},Класс:{}'.format(self.id, self.name,self.author,self.clas)
            
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hows_book = models.ManyToManyField(Books)
    debt = models.IntegerField(blank=True, null=False, verbose_name='Задолжность',default=0)
    
    
    def user_id(self):
        return str(self.user)
        
    def debt_result(self):
        self.debt=0
        return str(self.debt)
        
    def getbook(self):
        return str(self.hows_book.all())

    def decode(self):
        cap = cv2.VideoCapture(0)
        for i in range(30):
            cap.read()   
        ret, frame = cap.read()
        cv2.imwrite('./mysite/polls/static/media/images/decode_photo.png', frame)   
        cap.release()

        d=decode(Image.open('./mysite/polls/static/media/images/decode_photo.png'))
        d=str(d)
        start_index=d.find(':')
        end_index=d.find(',')
        result=d[start_index+1:end_index-1]
        if result == '':
            return 0
        else:
            return result


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userinfo.save()
