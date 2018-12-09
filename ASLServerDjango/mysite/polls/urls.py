from django.conf.urls import url

from .views import (
    generate_qr,
    BooksList,
    BookUpdate,
    BookDelete,
    users_home,
    BooksAdd,
)


urlpatterns = [
    url(r'^$', users_home, name='menu'),
    url(r'^list/$', BooksList.as_view(), name='books-list'),
    url(r'^add/$', BooksAdd.as_view(), name='books_add'),
    url(r'^(?P<pk>\d+)/update$', BookUpdate.as_view(), name='book_update'),
    url(r'^(?P<pk>\d+)/delete$', BookDelete.as_view(), name='book_delete'),
    # url(r'^give/$', BooksList.as_view(), name='bookslist'),    
    # url(r'^take/$', BooksList.as_view(), name='bookslist'),    
    url(r'^qr-code/(?P<book_id>[0-9]+)/$', generate_qr, name='generateqr'),    
]