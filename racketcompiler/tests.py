from django.test import TestCase
from app.models import Problem
from .racketcompiler import compile_and_run



class ParserTest(TestCase):
   def racket_problem_simulation(self):
       print(compile_and_run("s", "(define ( car-distance t) (* (/ 44 2.8) (* t t))) )","(check-within 500 500 0.001)"))
