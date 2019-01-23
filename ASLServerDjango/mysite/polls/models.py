import datetime
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
from django.contrib import admin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import qrcode
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractBaseUser):
    third_name = models.CharField(max_length=16)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30) 
    # if your additional field is a required field, just add it, don't forget to add 'email' field too.
    #REQUIRED_FIELDS = ['mobile', 'email'] 
    REQUIRED_FIELDS = ['username', 'first_name','last_name','third_name']
    USERNAME_FIELD =  'third_name'

class NewUser(models.Model):
    username = models.CharField(blank=False, null=False, max_length=200, verbose_name='Никнейм')
    password = models.CharField(blank=False, null=False, max_length=200, verbose_name='Пароль')
    password_raw =  models.CharField(blank=False, null=False, max_length=200, verbose_name='Повторите пароль')
    class Meta():
        verbose_name = 'Ученик'
        verbose_name_plural='Ученики'

BOOK=((1,'Учебник'),(2,'Художественная литература'))
class TypeBook(models.Model):
    options = models.CharField(max_length=100, blank = True, choices=BOOK)
'''
class Books_model(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Название')
    author = models.CharField(blank=False, null=False, max_length=200, verbose_name='Автор')
    clas = models.CharField(blank=False, null=False, max_length=200, verbose_name='Класс')
    num_izd = models.CharField(blank=False, null=False, max_length=200, verbose_name='Номер издания')
    name_izd = models.CharField(blank=False, null=False, max_length=200, verbose_name='Название издания')
    #pub_date = models.DateField('Дата добавления')
    quantity = models.IntegerField(blank=False, null=False, verbose_name='Количество книг')
    #qr_code_image = models.ImageField(upload_to='images/', null=False, blank=True)
    status = models.IntegerField(null = False,blank = False, verbose_name='Выдана книга(1) или нет(0)', default=0)
    #borrower = models.ForeignKey(User,blank=True, null=False, verbose_name='Вид книги')
    qr_code = models.ImageField(upload_to='images/', null=False, blank=True)
    class Meta():
        verbose_name = 'Одна Книга'
        verbose_name_plural = 'Одни Книги'

    def __str__(self):
        return 'id:{}, Название:{},Автор:{},Класс:{}'.format(self.id, self.name,self.author,self.clas)
'''
class Books(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Наименование')
    author = models.CharField(blank=False, null=False, max_length=200, verbose_name='Предмет')
    clas = models.CharField(blank=True, null=False, max_length=200, verbose_name='Класс',default = '')
    num_izd = models.CharField(blank=True, null=False, max_length=200, verbose_name='Номер издания',default='')
    name_izd = models.CharField(blank=True, null=False, max_length=200, verbose_name='Название издания',default='')
    #pub_date = models.DateField('Дата добавления')
    quantity = models.IntegerField(blank=False, null=False, verbose_name='Количество книг')
    #qr_code_image = models.ImageField(upload_to='images/', null=False, blank=True)
    status = models.IntegerField(null = False,blank = False, verbose_name='Выдана книга(1) или нет(0)', default=0)
    #borrower = models.ForeignKey(User,blank=True, null=False, verbose_name='Вид книги')
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
            
class UserProfile1(models.Model):
    MEDIA_CHOICES = (('1','A'),('2','B'))
    model = Books
    username = models.CharField(blank=False, null=False, max_length=200, verbose_name='Имя')
    fename = models.CharField(blank=False, null=False, max_length=200, verbose_name='Фамилия')
    third_name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Отчество')
    clas = models.CharField(blank=False, null=False, max_length=200, verbose_name='Класс')
    debt = models.IntegerField(blank=False, null=False, verbose_name='Задолжность')
    hows_book = models.ManyToManyField(Books)
    #hows_book = models.ForeignKey(Books, blank=True, default=None, null=True, verbose_name='Выдать ученику')
    def debt_result(self):
        return str(self.debt)
        
    def getbook(self):
        return str(self.hows_book)
     
    class Meta():
        verbose_name = "Ученик"
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return 'id:{}, Имя:{}, Фамилия:{}, Отчество:{}, Класс:{} ,Задолжность:{}'.format(self.id, self.username,self.fename,self.third_name,self.clas, self.debt) 

class Place(models.Model):
    name = models.CharField(max_length = 200 )
    keywords = models.CharField(max_length =200)

KITCHEN_OPTIONS = (
(1, 'Встроенная кухня'),
(2, 'Кухонная ниша'),
(3, 'Кухня-столовая'),
(4, 'Кухня-остров'),
(5, 'Открытая кухня'),
)

class Test(models.Model):
    options = models.CharField(max_length=100, blank = True, choices=KITCHEN_OPTIONS)
class User_Give_Book(models.Model):
    given_book = models.ManyToManyField(Test)

#class BookAdm(admin.ModelAdmin):
    #filter_horizontal=('hows_book',)
class AuthModel(models.Model):
    username = models.CharField(blank=False, null=False, max_length=200, verbose_name='ЛОГИН')
    password = models.CharField(blank=False, null=False, max_length=200, verbose_name='Пароль')

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
        # Включаем первую камеру
        cap = cv2.VideoCapture(0)

        # "Прогреваем" камеру, чтобы снимок не был тёмным
        for i in range(30):
            cap.read()

        # Делаем снимок    
        ret, frame = cap.read()

        # Записываем в файл
        cv2.imwrite('./mysite/polls/static/media/images/decode_photo.png', frame)   

        # Отключаем камеру
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



'''    
class Student(models.Model):
    choices = models.ManyToManyField(Books)
    third_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, unique=True)

class UserProfile(models.Model):
    username = models.CharField(blank=False, null=False, max_length=200, verbose_name='Имя')
    fename = models.CharField(blank=False, null=False, max_length=200, verbose_name='Фамилия')
    third_name = models.CharField(blank=False, null=False, max_length=200, verbose_name='Отчество')
    clas = models.CharField(blank=False, null=False, max_length=200, verbose_name='Класс')
    debt = models.IntegerField(blank=False, null=False, verbose_name='Задолжность')
    hows_book = models.ManyToManyField(Books)
    #hows_book = models.ManyToManyField(Books, blank=True, default=None, null=True, verbose_name='Выдать ученику')

 
    def __unicode__(self):
        return self.user
'''
