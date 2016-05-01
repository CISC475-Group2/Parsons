from django import forms
from app.models import Problem, Solved
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ProblemSubmissionForm(forms.Form):
    submission = forms.CharField()
    