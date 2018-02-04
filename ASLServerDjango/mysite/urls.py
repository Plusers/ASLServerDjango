from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from mysite.polls import views as polls_views


urlpatterns = [
    url(r'^$', polls_views.home, name='home'),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', polls_views.signup, name='signup'),

    url(r'^admin/', admin.site.urls),
]
