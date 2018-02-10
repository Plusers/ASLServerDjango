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
    
    def __str__(self):
        return self.books_name, self.books_author, self.books_class, self.books_numIzd, self.books_nameIzd
    