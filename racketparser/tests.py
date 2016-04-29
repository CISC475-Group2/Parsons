from django.test import TestCase
from .parser import read_parse_string_to_list, parse

class ParserTest(TestCase):
    def test_parser_passes(self):
        """runs passing test (known ouputs against known inputs expecting those outputs)."""
        self.assertEqual(
                "( <nt> <nt> )|( <nt> <nt> )|test|( <nt> <nt> <nt> )|1|2|( <nt> <nt> )|3|4|( <nt> <nt> <nt> )|+|2|3|",
                parse("( test(1 2 (3 4))) \n (+ 2 3)"))

        self.assertEqual(
                [['(', '<nt>', ')'], [['(', '<nt>', '<nt>', '<nt>', ')'],
                    [['-']], [['2']], [['(', '<nt>', '<nt>', ')'], [['3']], [['2']]]]],
                read_parse_string_to_list(parse("(- 2 (3 2))")))

    def test_parser_raises_exceptions(self):
        """runs tests expecting exceptions from input known to generate said exceptions."""
        #empty input test
        self.assertRaises(SyntaxError, parse, "")
        #unbalenced parenthesis
        self.assertRaises(SyntaxError, parse, "( test( 1 2)))")
        self.assertRaises(SyntaxError, parse, "( test( 1 2)")
        self.assertRaises(SyntaxError, parse, ')')
