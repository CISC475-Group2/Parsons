from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'accounts/login.html'}),
    url(r'^register/$',
        views.register_student,
        name='register_student'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}),
]
