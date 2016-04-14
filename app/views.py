from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Problem, Student, Solved

@login_required
def index(request):
    context = {}
    if request.user:
        solved_problem_ids = ()
        for s in Solved.objects.filter(user=request.user):
            solved_problem_ids = solved_problem_ids + (s.problem_id,)
        context['solved_problems'] = Problem.objects.filter(id__in=solved_problem_ids)

    return render(request, 'app/index.html', context)

@login_required()
def account(request):
    context = {}
    context['user'] = request.user

    return render(request, 'app/account.html', context)
