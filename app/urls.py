from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^account/$', views.account, name='account'),
    url(r'^problem/(?P<pk>[0-9]+)/$', login_required(views.ProblemView.as_view()), name='problem'),
]
