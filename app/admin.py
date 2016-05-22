from django.contrib import admin
from .models import Problem, Solved, Section, Student, Assignment

admin.site.register(Problem)
admin.site.register(Solved)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Assignment)