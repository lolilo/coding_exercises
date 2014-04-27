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
    res = []
    for i in range(len(l)):
            element = l[i]
            temp = l[:]
            temp.pop(i)

            temp_perms = permutList(temp)
            for r in temp_perms:
                # res.extend([[element] + r])
                res += [[element] + r]
    return res

def permutString(s):
    if not s:
            return ['']

    permutations = []
    for i in range(len(s)):
            element = s[i]
            temp = list(s[:])
            temp.pop(i)
            # temp = ''.join(temp)

            temp_perms = permutList(temp)
            for r in temp_perms:
                # permutations.extend([[element] + r])
                permutations += [[element] + r]
    return permutations

print permutList(range(3))

print permutString('pig')



