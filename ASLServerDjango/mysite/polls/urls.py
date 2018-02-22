from django.conf.urls import url

from .views import (
    BooksList,
    users_home,
)


urlpatterns = [
    url(r'^$', users_home, name='menu'),
    url(r'^list/$', BooksList.as_view(), name='books-list'),    
    # url(r'^add/$', BooksList.as_view(), name='bookslist'),

    # url(r'^give/$', BooksList.as_view(), name='bookslist'),    
    # url(r'^take/$', BooksList.as_view(), name='bookslist'),    
    # url(r'^qr-code/$', BooksList.as_view(), name='bookslist'),    
]