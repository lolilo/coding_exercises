#!/usr/bin/env python
import unittest

class Test(unittest.TestCase):
    def test_is_match_basic(self):
        self.assertEqual(is_match('aa*', 'a'), True)
        self.assertEqual(is_match('.*', ''), True)
        self.assertEqual(is_match('a.*', 'a'), True)
        self.assertEqual(is_match('.', 'a'), True)
        self.assertEqual(is_match('.*', 'anblskfj'), True)
        self.assertEqual(is_match('a*', 'anblskfj'), False)

        self.assertEqual(is_match('aa', ''), False)
        self.assertEqual(is_match('aaa', 'a'), False)

    def test_is_match_edge(self):
        self.assertEqual(is_match('a*', ''), True)
        self.assertEqual(is_match('z*b*', ''), True)
        self.assertEqual(is_match('.*j', 'anblskfj'), True)

        self.assertEqual(is_match('k', 'j'), False)
        self.assertEqual(is_match('.*k', 'j'), False)
        self.assertEqual(is_match('.*k', 'anblskfj'), False)

    def test_is_match_break(self):
        self.assertEqual(is_match('*', 'a'), False)
        self.assertEqual(is_match('a*aa', 'aa'), True)
        self.assertEqual(is_match('a.*c.*d', 'abcbcd'), True)
        self.assertEqual(is_match('a.*x.*d', 'abcbcd'), False)
        self.assertEqual(is_match('**bc', 'bc'), True) # breaks for odd number of stars. can implement checker to ignore extra stars


def current_chars_match(pattern, string, pi, si):
    return pattern[pi] == string[si] or pattern[pi] == '.'


def is_match(pattern, string, pi=0, si=0):
    len_pattern = len(pattern)
    len_string = len(string)

    if pi >= len_pattern: # no more pattern characters; check if there are remaining string
        return si >= len_string

    # next pattern char is not '*'; must string char match current pattern char
    # if pattern contains non-star char and string is empty, it is not a match
    if pi+1 >= len_pattern or (pi+1 < len_pattern and pattern[pi+1] != '*'):
        return si < len_string and current_chars_match(pattern, string, pi, si) and is_match(pattern, string, pi+1, si+1)

    # next pattern char is '*'
    while si < len_string and current_chars_match(pattern, string, pi, si):
        if is_match(pattern, string, pi+2, si): # brute force exhaustive search, non-greedy. if * matches zero chars
            return True
        # continue with next step in greedy algorithm
        si += 1
    return is_match(pattern, string, pi+2, si)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
