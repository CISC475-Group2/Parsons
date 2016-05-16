from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^account/$', views.account, name='account'),
    url(r'^problem/(?P<pk>[0-9]+)/$', views.problem, name='problem'),
    url(r'api/problem/(?P<pk>[0-9]+)/$', views.problem_detail),
    url(r'^classUpload/$', views.upload_file, name='upload'),
]
