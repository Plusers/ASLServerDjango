import datetime

import qrcode

from django.db import models
from django.utils import timezone


class OperationsWithBooks(models.Model):
    books_name = models.CharField(max_length=200)
    books_author = models.CharField(max_length=200)
    books_class = models.CharField(max_length=200)
    books_numIzd = models.CharField(max_length=200)
    books_nameIzd = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        img = qrcode.make(self.books_name+'/'+self.books_author+'/'+self.books_class+'/'+self.books_numIzd+'/'+self.books_nameIzd) 
        img.save("/home/vladislav/Документы/ASLServer/ASLServer/qr-users/"+self.books_name+".png")
        img.show()
        return self.books_name, self.books_author, self.books_class, self.books_numIzd, self.books_nameIzd

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    