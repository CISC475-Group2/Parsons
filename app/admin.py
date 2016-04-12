from django.contrib import admin
from .models import Problem, Block, Solved, Section, Student

admin.site.register(Problem)
admin.site.register(Block)
admin.site.register(Solved)
admin.site.register(Section)
admin.site.register(Student)
