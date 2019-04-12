from django.conf.urls import url

from .views import *


urlpatterns = [
    
    url(r'^$', users_home, name='menu'),
    url(r'^list/$', BooksList.as_view(), name='books-list'),#не выданные книги
    url(r'^search_losen/$', search_book, name='search_book'),#admin
    url(r'^add/$', bookadd, name='books_add'),#admin
    url(r'^(?P<pk>\d+)/update/$', BookUpdate.as_view(), name='book_update'),#admin
    url(r'^(?P<book_id>[0-9]+)/delete/$', bookdelete, name='book_delete'),#admin
    url(r'^all/$', BooksListAll.as_view(), name='bookslistall'), #все книги ученика   
    url(r'^pass/$', BooksListPass.as_view(), name='bookslistpass'), #выданные книги
    url(r'^qr-code/(?P<book_id>[0-9]+)/$', generate_qr, name='generateqr'),    
]