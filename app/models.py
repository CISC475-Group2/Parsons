import datetime, json

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from racketparser.parser import generate_parson_question

class Problem(models.Model):
    solution = models.TextField(default='')
    evaluates_to = models.TextField(default='')
    points = models.IntegerField(default=1)

    def solved(self, user):
        if Solved.objects.get(user_id=user.id, problem_id=self.id):
            return True
        else:
            return False

    def generate_initial_data(self):
        initial_data = {}
        initial_data['problem_number'] = self.pk
        initial_data['solution'] = self.solution
        initial_data['evaluates_to'] = self.evaluates_to
        initial_data['blocks'] = generate_parson_question(self.solution)

        return initial_data

    def __str__(self):
        return self.solution

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

