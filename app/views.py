from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Assignment, Problem, Student, Solved

# Django Rest Framework
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
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

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def problem_detail(request, pk):
    try:
        problem = Problem.objects.get(pk=pk)
    except Problem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProblemSerializer(problem)
        return JSONResponse(serializer.data)
