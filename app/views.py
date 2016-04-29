from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Assignment, Problem, Student, Solved

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProblemSerializer

@login_required
def index(request):
    context = {}

    if request.user:
        context['assignments'] = Assignment.objects.all();

    return render(request, 'app/index.html', context)

@login_required()
def account(request):
    context = {}
    context['user'] = request.user

    return render(request, 'app/account.html', context)

class ProblemView(generic.DetailView):
    model = Problem
    template_name = 'app/problem.html'

@api_view(['GET'])
def problem_detail(request, pk):
    try:
        problem = Problem.objects.get(pk=pk)
    except Problem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProblemSerializer(problem)
        return Response(serializer.data)
