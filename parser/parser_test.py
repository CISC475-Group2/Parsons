
import Parser
import unittest
class ParserTest(unittest.TestCase):
    def passing_test(self):
        """runs passing test (known ouputs against known inputs expecting those outputs)."""
        assert ("( <nt> <nt> )|( <nt> <nt> )|test|( <nt> <nt> <nt> )|1|2|( <nt> <nt> )|3|4|( <nt> <nt> <nt> )|+|2|3|"
                == (Parser.parse("( test(1 2 (3 4))) \n (+ 2 3)")))

        assert [['(', '<nt>', ')'], [['(', '<nt>', '<nt>', '<nt>', ')'],
                                     [['-']], [['2']], [['(', '<nt>', '<nt>', ')'], [['3']], [['2']]]]] == Parser.read_parse_string_to_list(Parser.parse("(- 2 (3 2))"))
    def exception_test(self):
        """runs tests expecting exceptions from input known to generate said exceptions."""
        #empty input test
        self.assertRaises(SyntaxError, Parser.parse, "")
        #unbalenced parenthesis
        self.assertRaises(SyntaxError, Parser.parse, "( test( 1 2)))")
        self.assertRaises(SyntaxError, Parser.parse, "( test( 1 2)")
        self.assertRaises(SyntaxError, Parser.parse, ')')

    def test(self):
        self.passing_test()
        self.exception_test()

testClass = ParserTest()
testClass.test()