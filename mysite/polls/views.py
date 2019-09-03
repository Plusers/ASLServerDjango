from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from django.contrib.auth.models import Group
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
import qrcode
from datetime import timedelta
import time
from django.conf import settings
import pandas as pd
from xlrd import *
import xlrd 
import collections as coll
import os
from django.contrib.auth.models import User
from mysite.polls.forms import *
from .forms import *
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets
from .serializers import BooksSerializer, UsersSerializer

#--------------------CHECKING------------------------



@login_required
def generate_qr(request, book_id):
    os.makedirs(".mysite/polls/static/media/images/", exist_ok=True)
    book_id = Books.objects.get(pk=book_id)
    filename = book_id.generate()
    user = User.objects.all()
    return render(request, 'generate_qr.html', {'book_id': book_id, 'filename':filename})

def user_infromation(request,user_id):
    model = User
    user_id = User.objects.get(pk=user_id)
    local_debt = 0
    for i in user_id.userinfo.hows_book.all():
        for j in Books.objects.all():
            if i!=j and i.status==0:
                j.status=0
                j.save()
            else:
                i.status=1
                i.save()
        j.save()
        i.save()
        local_debt+=1
    debt_result = user_id.userinfo.debt_result()
    user_id.userinfo.debt = str(int(debt_result)+local_debt)
    how_book = user_id.userinfo.hows_book.filter(status=1)
    return render(request, 'users_information.html', {'user_id':user_id, 'how_book':how_book})

class BooksList(LoginRequiredMixin, ListView):
    print("------------START----------------")
    model = Books
    template_name = "books_list_unpass.html"
    def get_context_data(self, **kwargs):
        #
        context = super(BooksList, self).get_context_data()


        #context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.filter(status=0)

        return context

class BooksListAll(LoginRequiredMixin, ListView):
    mas_of_all_books=[]
    for book in Books.objects.all():
        final_str=str(book.name)+" "+str(book.author)+" "+str(book.clas)
        mas_of_all_books.append(final_str)
    final_massive = coll.Counter(mas_of_all_books)
    print(final_massive)
    for book in Books.objects.all():
        groups=BooksGroups()
        name= book.name
        author = book.author
        clas = book.clas
        search_str = str(book.name)+" "+str(book.author)+" "+str(book.clas)
        groups.name = name
        groups.author = author
        groups.clas = clas
        groups.quantity = int(final_massive[search_str])
        groups.save()
    model = Books
    template_name = "books_list.html"
    def get_context_data(self, **kwargs):
        #
        context = super(BooksListAll, self).get_context_data()

        #context = super().get_context_data(quantity=1)
        context['books'] = Books.objects.filter()  

        return context

class BooksListPass(LoginRequiredMixin, ListView):
    model = Books
    template_name = "books_list_pass.html"
    def get_context_data(self, **kwargs):
        #
        context = super(BooksListPass, self).get_context_data()

        #context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.filter(status=1)

        return context
@login_required
def general_page(request):
    return render(request, 'general_page.html')


@login_required
def news(request):
    news_all = News.objects.all()
    return render(request, 'news.html', {'news_all': news_all})

@login_required
def user_cabinet(request):
    models = User
    return render(request, 'user_cabinet.html')

class UsersInformation(LoginRequiredMixin, ListView):
    model = Books
    template_name = "books_list.html"
    def get_contet_data(self, **kwargs):
        #
        context = super(BooksList, self).get_context_data(**kwargs)
        #context = super().get_context_data(**kwargs)
        context['users'] = Books.objects.all()
        return context


class GiveBookList(ListView):
    model = Books
    template_name = "books_list.html"
    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = Books.objects.all()
        q = self.request.GET.get("q")
        if q:
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            return queryset.filter(Q(name__icontains=q)|
                                   Q(name=q))

        return queryset

class UsersListpass(LoginRequiredMixin, ListView):
    model=User
    template_name = "users_pass.html"
    def get_context_data(self, **kwargs):
        #
        context = super(UsersListpass, self).get_context_data()

        #context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()

        return context

def search_book(request):
    model=Books
    result=''
    if request.POST.get('isbn_scan') == '':
        qwerty = IsbnBookForm(request.POST)
        if qwerty.is_valid():
           isbn=qwerty.cleaned_data.get('quantity')
           isbn= str(isbn)
           for user in User.objects.all():
            for book in user.userinfo.hows_book.all():
                if int(isbn) == int(book.quantity):
                    return HttpResponseRedirect('/users/information/'+str(user.id))


    elif request.POST.get('scan') == '':
        result = request.user.userinfo.decode()
        for user in User.objects.all():
            for book in user.userinfo.hows_book.all():
                if int(result) == book.id:
                    return HttpResponseRedirect('/users/information/'+str(user.id))
    else:
        qwerty=IsbnBookForm()            
    return render(request, 'search_book.html', {'isbn_form':qwerty,'result':result})  

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/library/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        if self.user.is_superuser==True:
            login(self.request, self.user)
            return render(self.request, 'general_page.html')
        elif self.user.is_superuser==False:
            login(self.request, self.user)
            return render(self.request, 'general_page.html')
        
        
@login_required
def users_home(request):
    models = User
    user = User.objects.filter(pk=id)
   
    return render(request, 'admin_menu.html')

class BooksAdd(CreateView):
    model = Books
    fields = '__all__'
@login_required
def bookgive(request,user_id):
    model=Books
    chet=0
    mas=[]
    result=''
    user_ind = User.objects.get(pk=user_id)
    for i in user_ind.userinfo.hows_book.all():
        mas.append(i)
    if request.POST.get('isbn_scan') == '':
        qwerty = IsbnBookForm(request.POST)
        if qwerty.is_valid():
           isbn=qwerty.cleaned_data.get('quantity')
           isbn= str(isbn)
           book = Books.objects.get(quantity=int(isbn))
           book.give_date = datetime.date.today()
           mas.append(book)
           book.status=1
           user_ind.userinfo.debt+=1
           book.save()
           user_ind.userinfo.hows_book=mas
           if str(book.type_of_book) == '1':
                print('Учебник')
                date = datetime.date(2019,5,20)
                book.pass_date = date
                #book.pass_date = datetime.data(2019, 5,20)
                book.save()
           elif str(book.type_of_book) == '2':
                print('Художественная литература')
                today = datetime.date.today()
                print(today)
                book.pass_date = datetime.date.today()+timedelta(days=7)
                print('SOOO GOOD')
                book.save()

    elif request.POST.get('scan')=='':
        result = user_ind.userinfo.decode()
        print(result)
        if result!=0:
            book = Books.objects.get(pk=int(result))
            book.give_date = datetime.date.today()
            mas.append(book)
            book.status=1
            user_ind.userinfo.debt+=1
            book.save()
            user_ind.userinfo.hows_book=mas
            if str(book.type_of_book) == '1':
                print('Учебник')
                date = datetime.date(2019,5,20)
                book.pass_date = date
                #book.pass_date = datetime.data(2019, 5,20)
                book.save()
            elif str(book.type_of_book) == '2':
                print('Художественная литература')
                today = datetime.date.today()
                book.pass_date = datetime.date(today.year, today.mounth, today.day+7)
                print('SOOO GOOD')
                book.save()
            user_ind.save()
            #return HttpResponseRedirect('/users/information/'+str(user_ind.id))
        else:
            result = 'Отсканируйте еще раз'
    else:
        qwerty=IsbnBookForm()
    

    
    user_ind.userinfo.hows_book=mas
        #return HttpResponseRedirect('/users/information/'+user_id+'/')#/users/information/1/
    form =  user_ind.id
    return render(request, 'give_book.html', {'isbn_form':qwerty, 'form': form,'result':result})  
@login_required
def bookpass(request,user_id):
    model=Books
    result=''
    user_ind = User.objects.get(pk=user_id)
    if request.POST.get('isbn_scan') == '':
        
        qwerty = IsbnBookForm(request.POST)
        if qwerty.is_valid():
           print('GOOOD')
           isbn=qwerty.cleaned_data.get('quantity')
           isbn= str(isbn)
           form = user_ind.userinfo.hows_book.all()
           for i in form:
               if int(i.quantity)==int(isbn): 
                   print('I am in if')
                   book = Books.objects.get(quantity=i.quantity)
                   print(book)
                   book.status=0
                   i.status=0
                   user_ind.userinfo.debt-=1
                   user_ind.save()
                   i.save()
                   book.save()
                   #return HttpResponseRedirect('/users/information/'+str(user_ind.id))

    elif request.POST.get('scan') == '':
        try:
            result = user_ind.userinfo.decode()
            form = user_ind.userinfo.hows_book.all()
            for i in form:
                if i.id==int(result): 
                    book = Books.objects.get(pk=i.id)
                    book.status=0
                    i.status=0
                    user_ind.userinfo.debt-=1
                    user_ind.save()
                    i.save()
                    
                    book.save()
                    qwerty=''
                    #return HttpResponseRedirect('/users/information/'+str(user_ind.id))
        except:
            result = 'Отсканируйте еще раз'
            qwerty=''

    else:
        print('BADDD')
        qwerty=IsbnBookForm()

    user_ind.userinfo.hows_book=user_ind.userinfo.hows_book.filter(status=1)
    form = user_ind.id
    return render(request, 'pass_book.html', {'isbn_form':qwerty, 'form': form , 'result':result})  

@login_required
def user_books_list(request):
    username = request.user
    user = User.objects.get(username=username)
    form = user
    return render(request, 'user_books_list.html', {'form': form})
@login_required
def bookdelete(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
        book.delete()
        return HttpResponseRedirect('/') 
    except:
        return HttpResponseNotFound('<h1>Такая книга не найдена.</h1>')    
@login_required
def bookadd(request):
    if request.method == 'POST':
        qwerty = BooksForm(request.POST)
        if qwerty.is_valid():
            qwerty.pass_date = datetime.date.today()
            qwerty.give_date = datetime.date.today()
            qwerty.save()
            if request.POST.get('table') == '':
                start = time.time()
                ger = Books()
                rb = xlrd.open_workbook('/home/vladislav/Загрузки/tablewithbooks.xlsx')
                sheet = rb.sheet_by_index(0)
                row=[]
                for i in range(1,sheet.nrows):
                    r=sheet.row_values(i)
                    row.append(r)
                index = Books.objects.count()#последний индекс книги
                index+=1
                d=0
                #6-колиство книг
                #1-наименование
                #2-прежмет
                #0-класс
                #3-издательство
                for i in range(0,len(row)):
                    if int(row[i][7]==0):#количество
                        d=1
                    elif int(row[i][7])>1 and (int(row[i][0]==10) or int(row[i][0]==11)):#количество
                        for j in range(0,int(row[i][7])):#количество
                            index+=1
                            ger.id = index
                            ger.name = row[i][1]#Наименование
                            ger.author = row[i][2]#предмет
                            ger.clas = row[i][0]#класс
                            ger.num_izd='Нет'
                            ger.name_izd = row[i][3] #издательство
                            ger.quantity=1
                            ger.save()
                    elif int(row[i][7])==1:
                        index+=1
                        ger.id = index
                        ger.name = row[i][1]
                        ger.author = row[i][2]
                        ger.clas = row[i][0]
                        ger.num_izd='Нет'
                        ger.name_izd = row[i][3]
                        ger.quantity=1
                        ger.save()
                finish = time.time()
                result = finish-start


            '''
            quantity=qwerty.cleaned_data.get('quantity')
            #index = Books_model.objects.count()
            index = Books.objects.count()
            if index==0:
                index+=1
            #tom=Books_model()
            ger=Books()
            for i in range(index,quantity+index+1):
                tom.id=i
                tom.name=qwerty.cleaned_data.get('name')
                tom.author=qwerty.cleaned_data.get('author')
                tom.clas = qwerty.cleaned_data.get('clas')
                tom.num_izd=qwerty.cleaned_data.get('num_izd')
                tom.name_izd=qwerty.cleaned_data.get('name_izd')
                tom.status=0
                tom.quantity=0
                tom.save()
            if quantity>=1:
                ind=Books.objects.count()
                if ind==0:
                    ind+=1
                ger.id=ind
                ger.name=tom.name
                ger.author = tom.author
                ger.clas = tom.clas
                ger.num_izd=tom.num_izd
                ger.name_izd = tom.name_izd
                ger.quantity=quantity
                ger.save()
                '''
            return HttpResponseRedirect('/books/all/')

        '''
        qwerty = BooksForm(request.POST)
        if qwerty.is_valid():
            quantity=qwerty.cleaned_data.get('quantity')
            print(Books.create('qwerty','','','',''))
            Books.objects.create(1,'qwe')
            qwerty.save()
            print('Soo Good')
        return HttpResponseRedirect('/')
        '''
    else:
        newbook = BooksForm()
        #qwerty = BooksForm()
    return render(request, 'add_book.html', {'form': newbook})
    

def signup(request):
    if request.method == 'POST':
        
        #form = SignUpForm(request.POST)
        form = SignUpForm(request.POST)
        #userinfo_form = UserInfoForm(request.POST)
        if form.is_valid() :
            user = form.save()
            user.userinfo.debt = 0  
            user.userinfo.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            #user.userinfo.mail = str(email)
            user.email = str(email) 
            user = authenticate(username=username, password=raw_password)
            send_info = 'Данные для входа в систему Библиотека Школы 444'+'\n'+'Логин:'+str(username)+'\n'+'Пароль:'+str(raw_password)
            send_mail('Администрация Библиотеки Школы 444', str(send_info), settings.EMAIL_HOST_USER, [str(email)])
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def auth(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = login(username=username, password=raw_password)
            login(request, user)
    else:
        form = AuthForm()
    return render(request, 'login.html', {'form': form})

class BookUpdate(UpdateView):
    model = Books
    fields = '__all__'

class AddBookToUser(UpdateView):
    model =  Books
    fields = '__all__'

class BookDelete(DeleteView):
    model = Books
    success_url = reverse_lazy('')

class PlaceListView(ListView):
    model = Books
    '''
    book = Books.objects.get(pk=0)
    print(book.quantity)
    '''
    template_name = "books_list.html"
    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            return queryset.filter(Q(name__icontains=q)|
                                   Q(author=q))

        return queryset

class UsersListView(ListView):
    model = User
    #g=Group.objects.get(name = '11')

    #u = User.objects.get(pk=1) # Get the first user in the system
    #mobile = u.userinfo.third_name
    #print(mobile)
    template_name = "users_list.html"
    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super().get_queryset()
        fename = self.request.GET.get("fename")
        nickname = self.request.GET.get("nickname")
        if fename:
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            return queryset.filter(Q(username__icontains=fename)|
                                   Q(last_name=fename))
        if nickname:
            return queryset.filter(Q(username = nickname))
        return queryset

class UsersAdd(CreateView):
    model = User
    fields = '__all__'

#Serializing
#@login_required
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
#@login_required
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer






print('START CHECKING')
users = User.objects.all()
for user in users:
    books_of_user = user.userinfo.hows_book.all()
    for book in books_of_user:
        now = datetime.date.today()
        if book.pass_date == now:
            send_info = 'Сегодня вы должны сдать в библиотеку книгу:'+'\n'+'Название:'+book.name+'\n'+'Автор:'+book.author
            send_mail('Администрация Библиотеки Школы 444', str(send_info), settings.EMAIL_HOST_USER, [str(user.email)])
            print('yes')
                    
print('ENDING...')    
