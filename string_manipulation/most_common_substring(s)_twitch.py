def most_common_substring(s):
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
    
    max_count = 1
    count = 1
    out = substrings[0]

    i = 0
    while i < len(substrings) - 1:
        if substrings[i] == substrings[i+1]:
            count += 1
        else: # substrings are not equal
            if count > max_count:
                out = substrings[i]
                max_count = count
                count = 1
            else: # count not greater than max_count
                count = 1
        i += 1
    return out
