from django.conf.urls import url

from .views import (
    generate_qr,
    BooksList,
    BookUpdate,
    BookDelete,
    users_home,
    BooksAdd,
    bookadd,
)


urlpatterns = [
    
    url(r'^$', users_home, name='menu'),
    url(r'^list/$', BooksList.as_view(), name='books-list'),#all
    url(r'^add/$', bookadd, name='books_add'),#admin
    url(r'^(?P<pk>\d+)/update/$', BookUpdate.as_view(), name='book_update'),#admin
    url(r'^(?P<pk>\d+)/delete/$', BookDelete.as_view(), name='book_delete'),#admin
    # url(r'^give/$', BooksList.as_view(), name='bookslist'),    
    # url(r'^take/$', BooksList.as_view(), name='bookslist'),    
    url(r'^qr-code/(?P<book_id>[0-9]+)/$', generate_qr, name='generateqr'),    
]