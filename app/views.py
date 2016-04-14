from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Problem, Student

class IndexView(generic.ListView):
    template_name = 'app/index.html'
    context_object_name = 'problems'

    def get_queryset(self):
        return Problem.objects.all()

def account(request):
    context = {}

    if not request.user:
        context['error'] = 'Please log in!'
    else:
        context['user'] = request.user

    return render(request, 'app/account.html', context)
