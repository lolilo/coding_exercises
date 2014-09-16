
# returns the most common substring of length 2 from an input string
# time: O(n) one pass to make dict and find the max within the dict
# space: O(n)
def most_common_substring(s):
    if type(s) != str:
        print "Input must be a string type."
        return
    
    if len(s) < 2:
        print "Input string must be at least length 2."
        return 
        
    if len(s) == 2:
        return s
        
    d = {}
    curr_max_count = 0
    curr_max_substring = s[:1]
    
    for i in range(len(s) - 1): # already checked first substring and assigned it to curr_max_substring
        ss = s[i] + s[i+1]
        if ss in d:
            d[ss] += 1
            if d[ss] > curr_max_count:
                curr_max_count = d[ss]
                curr_max_substring = ss
        else: 
            d[ss] = 1

    return curr_max_substring

s = 'hawahahanonowaisthiswawa'
print most_common_substring(s)


# time: O(nlogn) because of sorting
# space: O(n) 
def most_common_substring_slower(s):
    if type(s) != str:
        print "Input must be a string type."
        return
    
    if len(s) < 2:
        print "Input string must be at least length 2."
        return 
        
    if len(s) == 2:
        return s

    substrings = []
    
    for i in range(len(s) - 1):
        ss = s[i] + s[i+1]
        substrings.append(ss)
    
    substrings.sort()
    
    max_count = 0
    count = 1
    out = substrings[0]

    i = 0
    while i < len(substrings) - 1:
        if substrings[i] == substrings[i+1]:
            count += 1
        else: # substrings are not equal
            # print substrings[i]
            # print count
            if count > max_count:
                out = substrings[i]
                max_count = count
            #     count = 1 # reset count = 1
            # else: # count not greater than max_count
            #     count = 1
            count = 1
        i += 1

    # EDGE CASE. BE CAREFUL. Very last substrings are most requent. 
    if count > max_count:
        out = substrings[-1]

    return out

print most_common_substring_slower(s)
