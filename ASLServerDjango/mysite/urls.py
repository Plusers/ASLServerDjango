from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

# from mysite.polls import views as polls_views
from mysite.polls.views import (
	BooksList,
    signup,
    users_home,

)



urlpatterns = [
    url(r'^accounts/profile/', users_home, name='users_home'),
	

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
  	url(r'^books/list/$', BooksList.as_view(), name='bookslist'),
      

    url(r'^admin/', admin.site.urls),
]
