from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import Assignment, Problem, Student, Solved
from django.core.urlresolvers import reverse
from .rosterParser import parse

# Django Rest Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProblemSerializer
from app.forms import UploadRosterForm
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

@login_required()
def problem(request, pk):
    context = {}
    context['problem'] = Problem.objects.get(pk=pk)

    return render(request, 'app/problem.html', context)

@api_view(['GET'])
def problem_detail(request, pk):
    try:
        problem = Problem.objects.get(pk=pk)
    except Problem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProblemSerializer(problem)
        return Response(serializer.data)

@staff_member_required
def upload_file(request):
    if request.method == 'POST':
        context = {}
        form = UploadRosterForm(request.POST, request.FILES)
        if form.is_valid():
            parse(file=request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadRosterForm()
    return render_to_response('app/classUpload.html', {'form': form},context_instance=RequestContext(request))