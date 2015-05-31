import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.docs = ["This is doc one.", "This is doc two.", "This is doc three."]
        self.words = ["doc", "two"]

    def test_find_docs(self):
        self.assertEqual(len(find_docs(self.docs, self.words)), 1)


def clean_word(word):
    return word.strip('.,:!?')


def get_doc_words(doc):
    words = doc.split()
    for word_index in xrange(len(words)):
        words[word_index] = clean_word(words[word_index])
    return words
 

def find_docs(docs, words): # list of strings, list of strings
    words = set(words)
    valid_docs = []
    for doc in docs:
        words_copy = words.copy()
        doc = get_doc_words(doc)
        for word in doc:
            if word in words_copy:
                words_copy.remove(word)
            if len(words_copy) == 0:
                valid_docs.append(doc)
    return valid_docs


if __name__ == '__main__':
    unittest.main()
