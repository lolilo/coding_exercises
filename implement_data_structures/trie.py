from pprint import pprint

# make a trie with given words
def make_trie(word_list):
    trie = {}

    for word in word_list:
        if type(word) != str:
            raise TypeError ("Please input strings.")
        temp_trie = trie
        for letter in word: 
            if not temp_trie.get(letter):
                temp_trie[letter] = {}
            temp_trie = temp_trie[letter]
        temp_trie = temp_trie.setdefault('_end_', '_end_')
    return trie

words = ['pineapple', 'pinecone', 'pikachu']
print pprint(make_trie(words))


# The method setdefault() is similar to get(), but will set dict[key]=default if key is not already in dict.
# temp_trie = temp_trie.setdefault(letter, {})
# same as

# if temp_trie.get(letter):
#     temp_trie = temp_trie[letter]
# else:
#     temp_trie[letter] = {}
#     temp_trie = temp_trie[letter]

# or 

# if not temp_trie.get(letter):
#     temp_trie[letter] = {}
# temp_trie = temp_trie[letter]
