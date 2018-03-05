from django.conf.urls import url

from .views import (
    gen,
    BooksList,
    users_home,
)


urlpatterns = [
    url(r'^$', users_home, name='menu'),
    url(r'^list/$', BooksList.as_view(), name='books-list'),
        
    # url(r'^add/$', BooksList.as_view(), name='bookslist'),

    # url(r'^give/$', BooksList.as_view(), name='bookslist'),    
    # url(r'^take/$', BooksList.as_view(), name='bookslist'),    
    url(r'^qr-code/(?P<book_id>[0-9]+)/$', gen, name='generateqr'),    
]