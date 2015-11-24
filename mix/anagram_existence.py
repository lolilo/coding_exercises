# ball, balk, cats, ... zany
# labl => True, zyzy => False
# can preprocess list

def preprocess_list(l):
    new_list = []
    for item in l:
        new_list.append(create_hash_map(item))
    return new_list
        

def create_hash_map(word):
    h = {}
    for letter in word:
        if h.get(letter):
            h[letter] += 1
        else:
            h[letter] = 1
    return h


def anagram_is_in_list(word, l):
    # O(# num of words in list)
    #     O(#num of letters)
    # O(n*m)
    # O(m log m)
    # O(m) + O(1)
    
    # "abcd"
    # O(m) * O(1)
    # { a: 1, b: 1, l:2 } ball => ???
    # { a: 1, b: 1, c:1 , d:1 } 
    # { b: 1, l: 1, k: 1, u:1 } bulk => ???
    
    # "a1b1c0d0e0f0g0h0i0j0k0l2...z0" => ball
    # "a1b1c0...l1...z0"
    
    hash_map_of_word = create_hash_map(word)
    if hash_map_of_word in l:
        return True
    else:
        return False


def preprocess_list2(word_list):
    anagram_set = set()
    for word in word_list:
        alphabetized_word = ''.join(sorted(word)) #O(nlogn)
        anagram_set.add(alphabetized_word)
    return anagram_set


def anagram_is_in_list2(word, word_set):
    sorted_word = ''.join(sorted(word))
    if sorted_word in word_set:
        return True
    else:
        return False

    
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.word_list = ['ball', 'bulk', 'cats', 'dogs', 'flea', 'yaks', 'zany']
        self.processed_word_list = [{'a': 1, 'b': 1, 'l': 2}, {'k': 1, 'b': 1, 'u': 1, 'l': 1}, {'a': 1, 's': 1, 'c': 1, 't': 1}, {'g': 1, 's': 1, 'd': 1, 'o': 1}, {'a': 1, 'e': 1, 'l': 1, 'f': 1}, {'y': 1, 'a': 1, 'k': 1, 's': 1}, {'a': 1, 'y': 1, 'z': 1, 'n': 1}]
        self.processed_word_set = set(  ['anyz',
                                        'abll',
                                        'acst',
                                        'bklu',
                                        'aefl',
                                        'aksy',
                                        'dgos'])

    def test_preprocess_list(self):
        self.assertEqual(preprocess_list(self.word_list), self.processed_word_list)

    def test_anagram_is_in_list(self):
        self.assertEqual(anagram_is_in_list('ball', self.processed_word_list), True)
        self.assertEqual(anagram_is_in_list('yes', self.processed_word_list), False)
        self.assertEqual(anagram_is_in_list('labl', self.processed_word_list), True)
        self.assertEqual(anagram_is_in_list('labl', []), False)

    def test_preprocess_list2(self):
        self.assertEqual(preprocess_list2(self.word_list), self.processed_word_set)
    
    def test_anagram_is_in_list2(self):
        self.assertEqual(anagram_is_in_list2('yes', self.processed_word_set), False)
        self.assertEqual(anagram_is_in_list2('labl', self.processed_word_set), True)
        self.assertEqual(anagram_is_in_list2('labl', set()), False)


# print create_hash_map('test')
# print preprocess_list(['ball', 'bulk', 'cats', 'dogs', 'flea', 'yaks', 'zany'])
# hashed_list = preprocess_list(['ball', 'bulk', 'cats', 'dogs', 'flea', 'yaks', 'zany'])
# print anagram_is_in_list('labl', hashed_list)
# print anagram_is_in_list('labl', [])

unittest.main()
