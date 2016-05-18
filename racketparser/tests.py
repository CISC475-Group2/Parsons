from django.test import TestCase
from app.models import Problem
from .parser import parse, generate_parson_question

class ParserTest(TestCase):
    def test_parser_passes(self):
        """runs passing test (known ouputs against known inputs expecting those outputs)."""
        self.assertEqual(
                "( <nt> <nt> )|test|( <nt> <nt> <nt> )|1|2|( <nt> <nt> )|3|4|",
                parse("( test(1 2 (3 4))) "))

        self.assertEqual([['(', '<nt>', '<nt>', '<nt>', ')'], ['-'], ['2'], ['(', '<nt>', '<nt>', '<nt>', ')'], ['+'], ['3'], ['2']], generate_parson_question("(- 2 (+ 3 2))"))

        self.assertEqual([['(', '<nt>', '<nt>', '<nt>', ')'], ['*'], ['7'], ['(', '<nt>', '<nt>', '<nt>', ')'], ['+'], ['5'], ['3']], generate_parson_question('(* 7 (+ 5 3))'))

        self.assertEqual([['(', '<nt>', '<nt>', '<nt>', ')'], ['*'], ['7'], ['(', '<nt>', '<nt>', '<nt>', ')'], ['+'], ['5'], ['3']], generate_parson_question('(* 7 (+ 5 3))'))

        self.assertEqual([['(', '<nt>', '<nt>', ')'], ['sqrt'], ['16']], generate_parson_question('(sqrt 16)'))

    def test_problem_generates_correct_blocks(self):
        p1 = Problem(solution='(+ (- 3 2) (* 2 5))', evaluates_to='11', points=5)
        b1 = p1.generate_initial_data()['blocks']
        self.assertEqual(b1, [['(', '<nt>', '<nt>', '<nt>', ')'], ['+'], ['(', '<nt>', '<nt>', '<nt>', ')'], ['-'], ['3'], ['2'], ['(', '<nt>', '<nt>', '<nt>', ')'], ['*'], ['2'], ['5']])

        p2 = Problem(solution='(sqrt 16)', evaluates_to='11', points=5)
        p2 = Problem(solution='(sqrt 16)', evaluates_to='11', points=5)
        b2 = p2.generate_initial_data()['blocks']
        self.assertEqual(b2, [['(', '<nt>', '<nt>', ')'], ['sqrt'], ['16']])

    def test_parser_raises_exceptions(self):
        """runs tests expecting exceptions from input known to generate said exceptions."""
        #empty input test
        self.assertRaises(SyntaxError, parse, "")
        #unbalenced parenthesis
        self.assertRaises(SyntaxError, parse, "( test( 1 2)))")
        self.assertRaises(SyntaxError, parse, "( test( 1 2)")
        self.assertRaises(SyntaxError, parse, ')')
3