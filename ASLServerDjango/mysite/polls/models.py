import datetime

import qrcode

from django.db import models
from django.utils import timezone


class Books(models.Model):
    books_name = models.CharField(max_length=200)
    books_author = models.CharField(max_length=200)
    books_class = models.CharField(max_length=200)
    books_numIzd = models.CharField(max_length=200)
    books_nameIzd = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    
    def __str__(self):
        return str("Название: "+self.books_name+"/Автор: "+self.books_author+"/Класс: "+self.books_class+"/Номер издания(например 2): "+self.books_numIzd+"/Название издания(например ФГОС): "+self.books_nameIzd)

    def was_published_recently(self):		
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
