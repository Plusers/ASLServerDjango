from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
import qrcode
import os
from mysite.polls.forms import SignUpForm
from .forms import NameForm
from .models import Books
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

@login_required
def generate_qr(request, book_id):
    os.makedirs("./qr-books", exist_ok=True)
    book_id = Books.objects.get(pk=book_id)
    filename = book_id.generate()
    return render(request, 'generate_qr.html', {'filename': filename})
    

class BooksList(LoginRequiredMixin, ListView):
    print("------------START----------------")
    model = Books
    template_name = "books_list.html"
    def get_context_data(self, **kwargs):
        #
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.filter(borrower = self.request.user)
        return context


@login_required
def users_home(request):
    return render(request, 'users_menu.html')

def table_with_books(request):
    return render(request, 'table_with_books.html')

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

def get_name(request):
    # if this is a POST request we need to process the form data
    #if request.method == 'POST':
        # create a form instance and populate it with data from the request:
    #    form = NameForm(request.POST)
        # check whether it's valid:
    #    if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
     #       return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    #else:
     #   form = NameForm()

    return render(request, 'admin.html')#, {'form': form})

class BookCreate(CreateView):
    model = Books
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Books
    fields = ['name', 'author', 'clas', 'num_izd', 'name_izd', 'pub_date', 'quantity', 'borrower']

class BookDelete(DeleteView):
    model = Books
    success_url = reverse_lazy('books')