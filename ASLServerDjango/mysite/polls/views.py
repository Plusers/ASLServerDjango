from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import qrcode
import os
from mysite.polls.forms import SignUpForm
from .forms import NameForm, SimpleForm
from .models import Books, Place, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.db.models import Q

@login_required
def generate_qr(request, book_id):
    os.makedirs("./qr-books", exist_ok=True)
    book_id = Books.objects.get(pk=book_id)
    filename = book_id.generate()
    print(filename)
    return render(request, 'generate_qr.html', {'filename': filename})

def user_infromation(request, user_id):
    user_id = User.objects.get(pk=user_id)
    res_of_book = user_id.getbook()
    print(res_of_book)
    debt_result = user_id.debt_result()
    if res_of_book !='None':
       user_id.debt = str(int(debt_result)+1)
    print(user_id.mas[1])
    return render(request, 'users_information.html', {'user_id':user_id})

class BooksList(LoginRequiredMixin, ListView):
    print("------------START----------------")
    model = Books
    template_name = "books_list.html"
    def get_context_data(self, **kwargs):
        #
        context = super(BooksList, self).get_context_data(**kwargs)
        #context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()
        return context

class UsersInformation(LoginRequiredMixin, ListView):
    print("------------START----------------")
    model = Books
    template_name = "books_list.html"
    def get_context_data(self, **kwargs):
        #
        context = super(BooksList, self).get_context_data(**kwargs)
        #context = super().get_context_data(**kwargs)
        context['users'] = Books.objects.all()
        return context


class GiveBookList(ListView):
    model = Books
    template_name = "give_book_list.html"
    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            return queryset.filter(Q(name__icontains=q)|
                                   Q(name=q))

        return queryset

@login_required
def users_home(request):
    return render(request, 'users_menu.html')

class BooksAdd(CreateView):
    model = Books
    fields = '__all__'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if user.is_superuser == True:
                print("-------------ADMIN--------------")
                return render('menu.html') 
            if user.is_superuser == False:
                print("-------------USER---------------")
                return render('users_menu.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def checkboxtesting(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get("Vlad"))
            if form.cleaned_data.get("Vlad") == True:
                print("GOOD")
            return render(request, 'checkbox_books.html', {'form':form})
    else:
        form = SimpleForm()
    return render(request, 'checkbox_books.html', {'form': form})

class BookUpdate(UpdateView):
    model = Books
    fields = ['name', 'author', 'clas', 'num_izd', 'name_izd', 'pub_date', 'quantity', 'borrower']



class BookDelete(DeleteView):
    model = Books
    success_url = reverse_lazy('books')

class PlaceListView(ListView):
    model = Books
    template_name = "books_list.html"
    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            return queryset.filter(Q(name__icontains=q)|
                                   Q(name=q))

        return queryset

class UsersListView(ListView):
    model = User
    template_name = "users_list.html"
    def get_queryset(self):
        # Получаем не отфильтрованный кверисет всех моделей
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
        # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
            return queryset.filter(Q(username__icontains=q)|
                                   Q(fename=q))
        return queryset

class UsersAdd(CreateView):
    model = User
    fields = '__all__'


