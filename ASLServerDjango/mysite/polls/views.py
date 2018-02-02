from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import UpdateView
from .models import OperationsWithBooks


class Add_book(UpdateView):

    model = OperationsWithBooks
    fields = ['name_of_book']
    template_name_suffix = '_add_book'


class BooksList(ListView):

    model = OperationsWithBooks

    def get_context_data(self, **kwargs):
        context = super(BooksList, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context