# needle in a haystack - determine whether one string (needle) appears in another string (haystack) 
# and return the starting index number in the haystack for where the needle first appears

needle = 'pokemon'
haystack = 'pokeasd;lfjsldehohopokeemonssldfjsljg;wwrw98hrldkngvxlkvje8odupokemonqweq;ksf;mcdaldflpokemosl;fjdsl'

# O(n * m), where m = lenth of needle, n = length of haystack
def in_haystack(needle, haystack):

    # go through each char
    # match char with given needle
    # if it ever breaks, start over

    # hm, but then you would need to backtrack
    # potentially n*2 
    # how to make this time efficient? 
    # regex. :p 

    # pattern = [needle]

    # hm, but does regex return the index for you? 


    for char_i in xrange(len(haystack)): # O(n)
        word = haystack[char_i : char_i + len(needle)] # off by one error!!!!!
        if needle == word: # O(m
            return char_i

    return 'Needle is not in haystack.'


import re
def regex_in_haystack(needle, haystack):
    result = re.search(needle, haystack)
    # print result.string

    if result: 
        return result.start()

    return 'Needle is not in haystack.'

print in_haystack(needle, haystack)
print regex_in_haystack(needle, haystack)