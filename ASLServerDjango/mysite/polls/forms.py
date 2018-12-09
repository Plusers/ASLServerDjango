from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mysite.polls.models import Books
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget


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

    def send_email(self):
        
        # send email using the self.cleaned_data dictionary
        pass
model = Books
a=[""]*len(Books.objects.all())
d={}
for i in range(0,len(Books.objects.all())):
    c=str(Books.objects.get(pk=i+1))
    ind_start = c.find('Название')
    ind_dvoe = c.index(':',ind_start)
    ind_zap = c.index(',',ind_dvoe)
    a[i] = c[ind_dvoe+1:ind_zap]
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
        print(mas[i])
    i+=1
t=str(mas[1])
for i in range(len(mas)//2):
    if str(mas[i]) == t:
        del(mas[i])
del(mas[-1])
print(tuple(mas))

FAVORITE_BOOKS_CHOICES=tuple(mas)


class SimpleForm(forms.Form):
    favorite_colors = forms.MultipleChoiceField(required=False,
        widget=CheckboxSelectMultiple, choices=FAVORITE_BOOKS_CHOICES)