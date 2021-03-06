# def addperm(x, l):
#     for i in range(len(l) + 1):
#         return [l[0:i] + [x] + l[i:]]

# def perm(l):
#     if len(l) == 0:
#         return [[]]
#     for y in perm(l[1:]):
#         for x in addperm(l[0], y):
#             return x

# l = range(3)
# print perm(l)


def permutList(l):
    if not l:
            return [[]]
    perms = []
    for i in range(len(l)):
            element = l[i]
            temp = l[:]
            temp.pop(i)

            temp_perms = permutList(temp)
            for r in temp_perms: # this never runs if we just have [] and not [[]]
                perms.append([element] + r)
                # perms.extend([[element] + r])
                # perms += [[element] + r]
    return perms

def permutString(s):
    # base case will only run if original input is an empty string
    # otherwise, we are recursively calling permutList for the rest of the function
    if not s:
            return ['']

    permutations = []
    for i in range(len(s)):
            element = s[i]
            temp = list(s[:])
            # print 'PRINT THIS', temp
            temp.pop(i)

            temp_perms = permutList(temp)
            for r in temp_perms:
                new_permutation = ''.join([element] + r)
                permutations.append(new_permutation)
                # new = [element] + r
                # permutations += [''.join(new)]
    return permutations

print permutList(range(3))

print permutString('pow')

print permutString('')



