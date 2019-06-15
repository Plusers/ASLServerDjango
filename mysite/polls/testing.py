from django.test import TestCase as tc 
from django.contrib.auth.models import User
#from .models import *

class UsersTest(tc):
	def Users():
		s='h'
		for i in range(1000):
			User.objects.create(username=s)
			s+='d'
		print(User.objects.all())
UsersTest.Users()