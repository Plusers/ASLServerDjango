from django.conf.urls import url

from .views import (
    generate_qr,
    BooksList,
    BookCreate,
    BookUpdate,
    BookDelete,
    get_name,
    users_home,
    table_with_books,
)


urlpatterns = [
    url(r'^$', users_home, name='menu'),
    url(r'^list/$', BooksList.as_view(), name='books-list'),
    url(r'^admin_my/$', get_name, name='admin_my'),
    url(r'^table_with_books/$', table_with_books, name='table_with_books'),
    url(r'^create/$', BookCreate.as_view(), name='book_create'),
    url(r'^(?P<pk>\d+)/update$', BookUpdate.as_view(), name='book_update'),
    url(r'^(?P<pk>\d+)/delete$', BookDelete.as_view(), name='book_delete'),
    # url(r'^give/$', BooksList.as_view(), name='bookslist'),    
    # url(r'^take/$', BooksList.as_view(), name='bookslist'),    
    url(r'^qr-code/(?P<book_id>[0-9]+)/$', generate_qr, name='generateqr'),    
]