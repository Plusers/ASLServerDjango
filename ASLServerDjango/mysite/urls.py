from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.views.generic.base import RedirectView

from mysite.polls.views import signup, PlaceListView, UsersListView, UsersAdd, user_infromation, GiveBookList, checkboxtesting


urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='books:menu'), name='index'),    

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^checkboxtesting/$', checkboxtesting, name='checkboxtesting'),

    url(r'^users/list/$',UsersListView.as_view() , name='users_list'),
    url(r'^users/add/$', UsersAdd.as_view(), name='Users_add'),
    url(r'^users/give_book/$', GiveBookList.as_view(), name='GiveBookList'),
    url(r'^users/information/(?P<user_id>[0-9]+)/$', user_infromation, name='user_infromation'),

    url(r'^books/', include('mysite.polls.urls', namespace='books')),
    url(r'^books_search/$', PlaceListView.as_view(), name='books_search'),
    url(r'^users_search/$', UsersListView.as_view(), name='users_search'),
    url(r'^admin/', admin.site.urls),]
