import unittest
from prefixer import *

class TestPrefixer(unittest.TestCase):

    def setUp(self):
        pass

    # def test_infix_to_prefix(self):
    #     self.assertEqual(infix_to_prefix('3'), '3')
    #     self.assertEqual(infix_to_prefix('1 + 1'), '(+ 1 1)')
    #     self.assertEqual(infix_to_prefix('2 * 5 + 1'), '(+ 1 (* 2 5))')
    #     self.assertEqual(infix_to_prefix('2 * ( 5 + 1 )'), '(* (+ 1 5) 2)')
    #     self.assertEqual(infix_to_prefix('3 * x + ( 9 + y ) / 4'), '(+ (* 3 x) (/ (+ 9 y) 4))')

    def test_infix_to_postfix(self):
        self.assertEqual(infix_to_postfix('3'), '3')
        self.assertEqual(infix_to_postfix('1 + 1'), '(1 1 +)')
        self.assertEqual(infix_to_postfix('2 * 5 + 1'), '((2 5 *) 1 +)')
        self.assertEqual(infix_to_postfix('2 * ( 5 + 1 )'), '(2 (5 1 +) *)')
        self.assertEqual(infix_to_postfix('3 + 4 * 2'), '(3 (4 2 *) +)')
        self.assertEqual(infix_to_postfix('3 * 4 - 2'), '((3 4 *) 2 -)')
        self.assertEqual(infix_to_postfix('3 * 1 + ( 9 + 1 ) / 4'), '((3 1 *) ((9 1 +) 4 /) +)')
    
    def test_parse(self):
        self.assertEqual(parse('3 * 4 - 2'), ['3', '*', '4', '-', '2'])

    def test_create_ast(self):
        self.assertEqual(create_ast('3 * 4 - 2'), [[['3', '4', '*'], '2', '-']])
        self.assertEqual(create_ast('3 * 2'), [['3', '2', '*']])

    def test_ast_to_postfix(self):
        self.assertEqual(ast_to_postfix([['3', '4', '*'], '2', '-']), '((3 4 *) 2 -)')
    

if __name__ == '__main__':
    unittest.main()