from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from mysite.polls.forms import SignUpForm

from .models import Books


class Add_book(UpdateView):
    model = Books
    fields = ['name','autor', 'class', 'numIzd', 'nameIzd']
    template_name_suffix = '_add_book'


class BooksList(ListView):
    model = Books

    def get_context_data(self, **kwargs):
        context = super(BooksList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
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
            if is_superuser == True:
                return redirect('admin_home') 
            else:
                return redirect('users_home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
    