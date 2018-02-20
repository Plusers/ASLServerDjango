from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from mysite.polls.forms import SignUpForm

from .models import Books


class Add_book():
    model = Books
    fields = ['name','autor', '_class', 'numIzd', 'nameIzd','borrower']
    template_name_suffix = '_add_book'



class BooksList(ListView):
    model = Books
    template_name = "books_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['books'] = Books.objects.filter(borrower = request.user)
        return context


@login_required
def admin_home(request):
    return render(request, 'menu.html')

def users_home(request):
    return render(request, 'users_menu.html')



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
                return render('menu.html') 
            else:
                return render('users_menu.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
    