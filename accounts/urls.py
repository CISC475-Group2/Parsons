from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={'template_name': 'accounts/login.html'}),
    url(r'^register/$', views.register_student, name='register_student'),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': '/'}),
]
