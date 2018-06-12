from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.views.generic.base import RedirectView

from mysite.polls.views import signup


urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='books:menu'), name='index'),    

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),

    url(r'^books/', include('mysite.polls.urls'), name='books'),

    url(r'^admin/', admin.site.urls),
]
