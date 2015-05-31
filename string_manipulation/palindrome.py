# def is_palindrome(str):
#     i = 0
#     half_length = len(str) / 2
#     while i < half_length:
#         if not (str[i] == str[-i - 1]):
#             return False
#         i += 1
#     return True

def is_palindrome(str):
    i = 0
    half_length = len(str) / 2
    for i in xrange(half_length):
        if not (str[i] == str[-i - 1]):
            return False
    return True

str1 = 'tacocat'
str2 = 'abba'

print is_palindrome(str1)
print is_palindrome(str2)
print is_palindrome("not one")
