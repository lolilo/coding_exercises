# Given a list of integers, determine if any two numbers in the list
# sum to zero. Returns True if there exists such a pair.


# Given a list of words, print the words a) in ascending order of length.
# b) in alphabetic order in ascending order of length

l = ['aaaaaaa', 'e', 'popo', 'nono', 'aaaaaaaaa', 'a', 'h','agirl']

def print_asc(l):
    d = {}
    for i in l:
        target_key = len(i)
        if d.get(target_key):
            d[target_key].append(i)
        else:
            d[target_key] = [i]
    
    sorted_keys = d.keys()
    sorted_keys.sort()
    
    for i in sorted_keys:
        d[i].sort()
        for n in d[i]:
            print n
print_asc(l)

# Given a list of words, return a list of words with duplicates removed.

l = ['aaaaaaa', 'e', 'popo', 'a', 'nono', 'aaaaaaaaa', 'a', 'h','agirl', 'agirl']

def remove_dup(l):
    out = []
    d = {} # for checking duplicates. It's like a set data structure!
    for i in l:
        if d.get(i):
            # check if it already exists in the dictionary
            continue
        else:
            d[i] = 1
            out.append(i)
    return out
 
print remove_dup(l)
