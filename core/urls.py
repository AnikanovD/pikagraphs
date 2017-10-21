from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.users, name='index'),
    url(r'^users/$', views.users, name='users'),
    url(r'^user/(?P<username>[a-zA-Z0-9\._]{1,20})/$', views.user, name='user'),
    url(r'^secret_page_for_l4rever/$', views.secret_page_for_l4rever,
        name='secret_page_for_l4rever'),
    url(r'^OK/$', views.OK, name='OK')
]
