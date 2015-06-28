"""
regex function, subset
char a - z
. 
*
"""

import unittest

class Test(unittest.TestCase):
    def xtest_regex_basic(self):
        self.assertEqual(regex('aa*', 'a'), True)
        self.assertEqual(regex('a.*', 'a'), True)
        self.assertEqual(regex('.', 'a'), True)
        self.assertEqual(regex('.*', 'anblskfj'), True)
        self.assertEqual(regex('a*', 'anblskfj'), False)
        self.assertEqual(regex('aaa', 'a'), False)
    def test_regex_edge(self):
        self.assertEqual(regex('a*', ''), True)
        self.assertEqual(regex('z*b*', ''), True)
        self.assertEqual(regex('.*j', 'anblskfj'), True)
        self.assertEqual(regex('.*k', 'anblskfj'), False)
    def test_regex_break(self):
        self.assertEqual(regex('*', 'a'), False)
        self.assertEqual(regex('a*aa', 'aa'), True)


def isMatch(pattern_char, string_char):
    return pattern_char == string_char or pattern_char == '.'


def regex(pattern, string):
    pi = 0
    si = 0
    len_pattern = len(pattern) # do this so that we don't need to calculate length each time
    len_string = len(string)

    while pi < len_pattern and si < len_string:
        current_pattern_char = pattern[pi]
        if current_pattern_char == '*':
            # assume that pattern will not start with a *; there will always be a char before it
            prev_pattern_char = pattern[pi - 1]
            while si < len_string and isMatch(prev_pattern_char, string[si]):
                si +=1
            pi += 1

        elif isMatch(current_pattern_char, string[si]):
            pi += 1
            si += 1

    # at this point, check if we are in a valid state
    # if we haven't consumed all of the input s, we know it's invalid
    if si < len_string:
        return False

    def check_trailing_star_and_empty_string(pi):
        # a*, a*b* and '' are valid
        # aaaaa and a are not valid
        while pi < len_pattern:
            if pi + 1 < len_pattern and pattern[pi + 1] == '*': # this is valid
                pi += 2
                # assume not multiple repeat in pattern. ex. a**
            else: # not _* 
                return False
        return True

    # 'a*aa', 'aa'
    def check_last_chars_before_star_match(pattern, string):
        if len(string) == 0:
            return True
        pi, si = -1, -1
        while pattern[pi] != '*' and pi > - len_pattern:
            current_last_pattern_char = pattern[pi]
            current_last_string_char = string[si]
            if isMatch(current_last_pattern_char, current_last_string_char):
                pi -= 1
                si -= 1
            else:
                return False
        return True

    # print 'this is string', string
    # print 'check_trailing_star_and_empty_string', check_trailing_star_and_empty_string(pi)
    # print 'check_last_chars_before_star_match', check_last_chars_before_star_match(pattern, string)
    return check_last_chars_before_star_match(pattern, string) or check_trailing_star_and_empty_string(pi)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
