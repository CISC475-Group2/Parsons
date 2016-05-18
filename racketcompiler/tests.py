from django.test import TestCase
from app.models import Problem
from .racketcompiler import compile_and_run



class CompilerTest(TestCase):
   def test_racket_problem_simulation(self):
        p = Problem(solution='(- 2 (+ 3 2))',test_code="(check-within 500 500 0.001)")
        self.assertEqual(compile_and_run(p, "(define ( car-distance t) (* (/ 44 2.8) (* t t))) ")[0],"failed")
