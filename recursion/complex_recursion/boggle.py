DICTIONARY_PATH = 'words.txt'

grid = "fxie amlo ewbx astu".split()
nrows, ncols = len(grid), len(grid[0])

# A dictionary word that could be a solution must use only the grid's
# letters and have length >= 3. (With a case-insensitive match.)
import re
alphabet = ''.join(set(''.join(grid)))
# valid_boggle = re.compile('[' + alphabet + ']{3,}$', re.I).match # returns None if string does not match pattern
# # valid_boggle is a function -- not great b/c we're doing work each time it's called


pattern = '[' + alphabet + ']{3,}$'
re_object = re.compile(pattern, re.I)
def valid_boggle(re_object, word):

	if re_object.match(word):
		return True
	else:
		return False

input_file = open(DICTIONARY_PATH)
set_of_words = set(input_file.read().splitlines()) # assume no blank lines in input file

valid_set_of_words = set()
for word in set_of_words:
	if valid_boggle(re_object, word):
		valid_set_of_words.add(word)

print valid_set_of_words

# can also do list_of_words = input_file.readline().strip() with a for-loop 
# to individually filter out lines for blanks and other invalid data


