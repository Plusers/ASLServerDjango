from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mysite.polls.models import Books, UserInfo
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget
import datetime

class AuthForm(forms.Form):
    username = forms.CharField(max_length=30, required=False, help_text='Optional.',label='Логин')
    password = forms.CharField(max_length=30, required=False, help_text='Optional.',label='Пароль')
    class Meta:
        model = User
        fields = ('username','password')        
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False,label='Логин*')
    email = forms.EmailField(max_length=30, required=False,label='Почта*')
    first_name = forms.CharField(max_length=30, required=False,label='Имя*')
    last_name = forms.CharField(max_length=30, required=False,label='Фамилия*')
    password1 = forms.CharField(widget=forms.PasswordInput,max_length=30, required=False,label='Пароль*')
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','password1', 'password2', )
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields=('hows_book','debt')
BOOK=(('Учебник'),('Художественная литература'))
class BooksForm(forms.ModelForm):
    name = forms.CharField(label='Название', max_length=100)
    author = forms.CharField(label='Автор', max_length=100)
    clas = forms.CharField(label='Класс', required=False, max_length=100)
    num_izd = forms.CharField(label='Номер издания', required=False, max_length=100)
    name_izd = forms.CharField(label='Название издания', required=False, max_length=100)
    #pub_date = forms.DateField('Дата добавления')
    quantity = forms.CharField(label='ISBN-код')
   # options = forms.ChoiceField(choices=BOOK, label='Вид книги:')

    class Meta:
        model=Books#Books_model
        fields = ('name','author', 'clas', 'type_of_book', 'num_izd', 'name_izd', 'quantity')#'options')
class IsbnBookForm(forms.ModelForm):
    quantity= forms.CharField(label='ISBN-код')

    class Meta:
        model = Books
        fields = ('quantity', )
'''
model = Books
a=[""]*len(Books.objects.all())
d={}
for i in range(0,len(Books.objects.all())):
    c=str(Books.objects.get(pk=i+1))
    a[i] = c
    d[str(i+1)] = a[i]
final = ['']*len(Books.objects.all()) 
u=()  

for key,value in d.items():
    final +='('+ key+','+"'"+value+"'"+'),'
    u = u+tuple((key,value))
mas =[()]*len(u)
i=0
while i!=len(u):
    if i%2==0:
        mas[i] = tuple((u[i],u[i+1]))
    i+=1
if len(mas)!=0:
    t=str(mas[1])
    for i in range(len(mas)//2):
        if str(mas[i]) == t:
            del(mas[i])
    del(mas[-1])
    FAVORITE_BOOKS_CHOICES=tuple(mas)
else:
    FAVORITE_BOOKS_CHOICES = (('0',1),('1',2))
    '''
class GiveBookForm(forms.ModelForm):
    model=Books
    hows_book = forms.ModelMultipleChoiceField(queryset=Books.objects.filter(status=0), label="Выберите книги", widget=forms.CheckboxSelectMultiple) 
    #hows_book = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_BOOKS_CHOICES,required=False)
    #hows_book = forms.MultipleChoiceField(choices=Books.objects.all(),required=False)
    def __init__(self, *args, **kwargs):
                super(GiveBookForm, self).__init__(*args, **kwargs)
                self.fields['hows_book'].queryset=Books.objects.filter(status=0)
    class Meta:
        model = UserInfo
        fields = ('hows_book',)
 
class PassBookForm(forms.ModelForm):
    def user_index(user_id):
        return user_id
    def pass_book(user_id):
        hows_book = forms.ModelMultipleChoiceField(queryset=user_id.userinfo.hows_book.all(), label="Выберите книги", widget=forms.CheckboxSelectMultiple) 
        #hows_book = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_BOOKS_CHOICES,required=False)
        #hows_book = forms.MultipleChoiceField(choices=Books.objects.all(),required=False)
        def __init__(self, *args, **kwargs):
                    super(GiveBookForm, self).__init__(*args, **kwargs)
                    self.fields['hows_book'].queryset=user_id.userinfo.hows_book.all()
        return hows_book
    
    model=Books
       
    class Meta:
        model = UserInfo
        fields = ('hows_book',)
