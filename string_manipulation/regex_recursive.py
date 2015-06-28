#!/usr/bin/env python
import unittest

class Test(unittest.TestCase):
    def test_isMatch_basic(self):
        self.assertEqual(isMatch('aa*', 'a'), True)
        self.assertEqual(isMatch('.*', ''), True)
        self.assertEqual(isMatch('a.*', 'a'), True)
        self.assertEqual(isMatch('.', 'a'), True)
        self.assertEqual(isMatch('.*', 'anblskfj'), True)
        self.assertEqual(isMatch('a*', 'anblskfj'), False)

        self.assertEqual(isMatch('aa', ''), False)
        self.assertEqual(isMatch('aaa', 'a'), False)
    def test_isMatch_edge(self):
        # self.assertEqual(isMatch('a*', ''), True)
        # self.assertEqual(isMatch('z*b*', ''), True)
        # self.assertEqual(isMatch('.*j', 'anblskfj'), True)

        self.assertEqual(isMatch('k', 'j'), False)
        self.assertEqual(isMatch('.*k', 'j'), False)
        # self.assertEqual(isMatch('.*k', 'anblskfj'), False)
    def xtest_isMatch_break(self):
        self.assertEqual(isMatch('*', 'a'), False)
        self.assertEqual(isMatch('a*aa', 'aa'), True)
        self.assertEqual(isMatch('a.*c.*d', 'abcbcd'), True)
        # self.assertEqual(regex('a.*x.*d', 'abcbcd'), False) # Breeealdskfjas;ldfjk -- go with recursive solution. :(


def current_chars_match(pattern, string, pi, si):
    return pattern[pi] == string[si] or pattern[pi] == '.'

def is_match(pattern, string, pi, si):
    len_pattern = len(pattern)
    len_string = len(string)

    if pi >= len_pattern: # no more pattern characters; check if there are remaining string
        return si >= len_string

    print si, pi
    # next pattern char is not '*'; must string char match current pattern char
    # if pattern contains non-star char and string is empty, it is not a match
    if pi+1 < len_pattern and pattern[pi+1] != '*':
        return si < len_string and current_chars_match(pattern, string, pi, si) and is_match(pattern, string, pi+1, si+1)

    # next pattern char is '*'
    while si < len_string and current_chars_match(pattern, string, pi, si):
        if is_match(pattern, string, pi+2, si): # brute force exhaustive search, non-greedy. if * matches zero
            return True
        si += 1
    return is_match(pattern, string, pi+2, si)


def isMatch(pattern, string):
    return is_match(pattern, string, 0, 0)

                          
def main():
    unittest.main()

if __name__ == "__main__":
    main()
