from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )

class NameForm(forms.Form):
    name_book = forms.CharField(label='Название книги', max_length=100)
    author = forms.CharField(label='Автор', max_length=100)
    classic = forms.CharField(label='Класс', max_length=100)
    num_izd = forms.CharField(label='Номер издания', max_length=100)
    name_izd = forms.CharField(label='Название издания', max_length=100)
    quantity = forms.IntegerField(label='Количество')