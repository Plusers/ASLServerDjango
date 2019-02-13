from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
import qrcode
import time
from django.conf import settings
import pandas as pd
from xlrd import *
import xlrd 
import os
from django.contrib.auth.models import User
from mysite.polls.forms import SignUpForm, UserInfoForm
from .forms import *
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect



@login_required
def generate_qr(request, book_id):
    os.makedirs(".mysite/polls/static/media/images/", exist_ok=True)
    book_id = Books.objects.get(pk=book_id)
    filename = book_id.generate()
    print(filename)
    user = User.objects.all()
    print(user)
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
        print(i,i.status)
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
    print(User)
    Books.create("a","a","a","a","a")
    def get_context_data(self, **kwargs):
        #
        context = super(BooksList, self).get_context_data()

        #context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.filter(status=0)

        return context

class BooksListAll(LoginRequiredMixin, ListView):
    model = Books
    template_name = "books_list.html"
    def get_context_data(self, **kwargs):
        #
        context = super(BooksListAll, self).get_context_data()

        #context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()

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
def user_cabinet(request):
    models = User
    print(request.user.userinfo.debt)
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
    if request.POST.get('scan') == '':
        result = request.user.userinfo.decode()
        for user in User.objects.all():
            for book in user.userinfo.hows_book.all():
                if int(result) == book.id:
                    return HttpResponseRedirect('/users/information/'+str(user.id))
                
    return render(request, 'search_book.html', {'result':result})  

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/books/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        if self.user.is_superuser==True:
            login(self.request, self.user)
            return render(self.request, 'admin_menu.html')
        elif self.user.is_superuser==False:
            login(self.request, self.user)
            return render(self.request, 'user_menu.html')
        # Выполняем аутентификацию пользователя.
        
@login_required
def users_home(request):
    models = User
    user = User.objects.filter(pk=id)
    print(user)
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
    if request.POST.get('scan')=='':
        result = user_ind.userinfo.decode()
        try:
            book = Books.objects.get(pk=int(result))
            mas.append(book)
            book.status=1
            user_ind.userinfo.debt+=1
            book.save()
            user_ind.userinfo.hows_book=mas
            user_ind.save()
            return HttpResponseRedirect('/users/information/'+str(user_ind.id))
        except:
            result = 'Отсканируйте еще раз'
    print(mas)

    
    user_ind.userinfo.hows_book=mas
    print('now',user_ind.userinfo.hows_book.all())
        #return HttpResponseRedirect('/users/information/'+user_id+'/')#/users/information/1/
    form =  user_ind.id
    return render(request, 'give_book.html', {'form': form, 'result':result})  
@login_required
def bookpass(request,user_id):
    model=Books
    result=''
    user_ind = User.objects.get(pk=user_id)
    if request.POST.get('scan') == '':
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
                print('BOOK:',book.status)
                book.save() 
            else:
                result = 'Отсканируйте еще раз'
                
    print(user_ind.userinfo.hows_book.filter(status=1))
    user_ind.userinfo.hows_book=user_ind.userinfo.hows_book.filter(status=1)
    form = user_ind.id
    return render(request, 'pass_book.html', {'form': form , 'result':result})  
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
                print('Минут:',result//60,'Секунд:',result%60)
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
            return HttpResponseRedirect('/books/list/')
            
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
        #tom=BooksForm()
        qwerty = BooksForm()
    return render(request, 'add_book.html', {'form': qwerty})
    

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
            '''
            userprofile = userinfo_form.save(commit=False)
            userprofile.user=user
            userprofile.hows_book=None
            userprofile.debt = 0
            userprofile.save()
            '''
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
        #userinfo_form=UserInfoForm()
    return render(request, 'signup.html', {'form': form})#, 'userinfo_form': userinfo_form})
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


