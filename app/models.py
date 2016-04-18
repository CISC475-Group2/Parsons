import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Problem(models.Model):
    question = models.TextField()
    solution = models.TextField()
    points = models.IntegerField(default=1)

    def __str__(self):
        return self.question

class Block(models.Model):
    problem = models.ForeignKey(Problem)
    code = models.TextField()

    def __str__(self):
        return 'Code block for problem ' + str(self.problem.id)

class Solved(models.Model):
    user = models.ForeignKey(User)
    problem = models.ForeignKey(Problem)
    solved_time = models.DateTimeField('solved time', default=timezone.now)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' solved problem ' + str(self.problem.id)

class Assignment(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    due_date = models.DateTimeField('due date', default=timezone.now() + datetime.timedelta(days=10))
    problems = models.ManyToManyField(Problem)

    def __str__(self):
        return self.title

class Section(models.Model):
    section = models.TextField()

    def __str__(self):
        return self.section

    # Generate available sections choices, to be used in forms
    def get_available_choices():
        sc = ()
        for section in Section.objects.all():
            sc = sc + ((section.section, section.section),)

        return sc

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' -- ' + self.user.email

