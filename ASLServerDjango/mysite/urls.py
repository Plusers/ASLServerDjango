from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from mysite.polls.views import *
from django.conf import settings


urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='books:menu'), name='index'),    
    url(r'^library/$', general_page, name='general-page'),
    url(r'^news/$', news, name='news-page'),
    #url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    #url(r'^login/$', auth, name='login'),

    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', signup,name='signup'),

    url(r'^users/list/$',UsersListView.as_view() , name='users_list'),#admin
    url(r'^users/list-pass/$',UsersListpass.as_view() , name='users_list_pass'),#admin
    url(r'^users/books/$',user_books_list , name='user_books_list'),#admin
    url(r'^user/cabinet/$',user_cabinet , name='user_cabinet'),#admin
    url(r'^users/(?P<user_id>\d+)/add/$', bookgive, name='Users_add_book'), #admin/users/{{user_id.id}}/give
    url(r'^users/(?P<user_id>\d+)/pass/$', bookpass, name='Users_pass_book'),
    url(r'^users/information/(?P<user_id>\d+)/$', user_infromation, name='user_infromation'),#admin
    url(r'^users/(?P<user_id>\d+)/update/$',AddBookToUser.as_view(),name='AddBookToUser'),#admin
    url(r'^books/$',PlaceListView.as_view(),name='bookslist'),
    url(r'^books/', include('mysite.polls.urls', namespace='books')),
    url(r'^books_search/$', PlaceListView.as_view(), name='books_search'),
    url(r'^users_search/$', UsersListView.as_view(), name='users_search'),#admin
    url(r'^admin/', admin.site.urls),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

