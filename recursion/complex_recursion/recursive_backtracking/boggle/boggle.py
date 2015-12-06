DICTIONARY_PATH = 'words.txt'

grid = "fxie amlo ewbx astu".split()
nrows, ncols = len(grid), len(grid[0])

# A dictionary word that could be a solution must use only the grid's
# letters and have length >= 3. (With a case-insensitive match.)
import re


# sets up words that may appear on board and their prefixes
def set_up(DICTIONARY_PATH): # could also pass in different Boggle rule/valid pattern
	alphabet = ''.join(set(''.join(grid)))
	# valid_boggle = re.compile('[' + alphabet + ']{3,}$', re.I).match # returns None if string does not match pattern
	# valid_boggle is a function -- not great b/c we're doing work each time it's called

	pattern = '[' + alphabet + ']{3,}$'
	re_object = re.compile(pattern, re.I)
	def valid_boggle(re_object, word):

		if re_object.match(word):
			return True
		else:
			return False

	input_file = open(DICTIONARY_PATH)
	set_of_words = set(input_file.read().splitlines()) # assume no blank lines in input file

	# can also do list_of_words = input_file.readline().strip() with a for-loop
	# to individually filter out lines for blanks and other non-bogglable data
	# this would also save us from constructing a separate set_of_words
	valid_set_of_words = set()
	for word in set_of_words:
		if valid_boggle(re_object, word):
			valid_set_of_words.add(word)

	###### We now have a list of valid words that could possibly appear on the Boggle board.######
	# print valid_set_of_words

	# create a set of word prefixes
	# could use a list comprehension here
	prefixes = set()
	for word in valid_set_of_words:
		for i in range(2, len(word) + 1):
			prefix = word[:i]
			prefixes.add(prefix)

	return valid_set_of_words, prefixes

words, prefixes = set_up(DICTIONARY_PATH)
# print words, '\n', prefixes

#### from StackOverflow...
# http://stackoverflow.com/questions/746082/how-to-find-list-of-possible-words-from-a-letter-matrix-boggle-solver#750012
def solve():
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            for result in extending(letter, ((x, y),)):
                yield result

def extending(prefix, path):
    if prefix in words:
        yield (prefix, path)
    for (nx, ny) in neighbors(path[-1]):
        if (nx, ny) not in path:
            prefix1 = prefix + grid[ny][nx]
            if prefix1 in prefixes:
                for result in extending(prefix1, path + ((nx, ny),)):
                    yield result

def neighbors((x, y)):
    for nx in range(max(0, x-1), min(x+2, ncols)):
        for ny in range(max(0, y-1), min(y+2, nrows)):
            yield (nx, ny)

solve()