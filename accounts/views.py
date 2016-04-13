from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import StudentRegistrationForm
from django.contrib.auth import login

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'accounts/register.html', {'form':form})
    else:
        form = StudentRegistrationForm()

    return render(request, 'accounts/register.html', {'form':form})
