from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import StudentRegistrationForm
from django.contrib.auth import login

def register_student(request):
    context = {'form': StudentRegistrationForm()}
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
            return render(request, 'accounts/register.html', context)

    return render(request, 'accounts/register.html', context)
