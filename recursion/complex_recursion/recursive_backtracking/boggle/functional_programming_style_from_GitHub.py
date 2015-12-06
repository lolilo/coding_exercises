# given a dictionary, prefixes, and a Boggle board, find all viable words in the board

# (x, y)
# (0, 0) is the left-top most corner
# T N N H A
# I G N E I
# S G E I B
# C A H N I
# O N F O E

# board is in the form
# {(1, 3): 'a', (3, 0): 'h', (2, 1): 'n', (0, 3): 'c', (4, 0): 'a', (1, 2): 'g', (3, 3): 'n', (4, 4): 'e', (0, 4): 'o', (4, 1): 'i', (1, 1): 'g', (3, 2): 'i', (0, 0): 't', (2, 2): 'e', (1, 4): 'n', (2, 3): 'h', (4, 2): 'b', (1, 0): 'n', (0, 1): 'i', (3, 1): 'e', (2, 4): 'f', (2, 0): 'n', (4, 3): 'i', (3, 4): 'o', (0, 2): 's'}

import optparse

MIN_LENGTH = 4
DICTIONARY = set()
PREFIXES = {}
WIDTH = 5
HEIGHT = 5
OFFSETS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
WORD_LIST_PATH = 'toy_words.txt'

def load_dictionary():
    global DICTIONARY
    global PREFIXES # in the form of nested dictionaries

    DICTIONARY = set()
    # with open(WORD_LIST_PATH) as f:
    f = open(WORD_LIST_PATH)
    for line in f:
        word = line.strip()
        if len(word) >= MIN_LENGTH and word.isalpha():
            DICTIONARY.add(word.lower())
    f.close()

    PREFIXES = {}
    for word in sorted(DICTIONARY):
        node = PREFIXES
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]

    print len(DICTIONARY), 'words loaded'
    print '----'

def is_prefix(prefix):
    node = PREFIXES
    for letter in prefix:
        if letter not in node:
            return False
        node = node[letter]
    return True

# starting off, positions_used = set(), prefix = ''. We pass this in via the original caller.
# update the prefix to include letter at current position
# if the updated prefix is not a valid prefix, return an empty set

# initialize a set(), found
# if prefix is in the word dictionary, add prefix to found
# keep track that we have used this current position, add it to the set positions_used
# for every possible valid offset / for every possible direction, recursively call find_words and update the set found
    # invalid are movements that go to a previously visited position / node or go off the boggle board
# remove current position from position_used to allow it for use in earlier recursive stack frames/calls
    # recursive backtracking?
# return the set found


# returns a set of found words
def find_words(board, positions_used, prefix, pos):
    prefix = prefix + board[pos] # update prefix
    if not is_prefix(prefix):
        # no words with this as a prefix
        return set() # return an empty set

    found = set() # this will update with words we find with prefix
    if prefix in DICTIONARY:
        found.add(prefix)

    positions_used.add(pos) # keep track that we have visited this coordinate

    for offset in OFFSETS:
        new_pos = (pos[0] + offset[0], pos[1] + offset[1])
        if new_pos in positions_used:
            continue
        if not (0 <= new_pos[0] < WIDTH and 0 <= new_pos[1] < HEIGHT):
            continue

        found.update(find_words(board, positions_used, prefix, new_pos)) #set.update(set)

    positions_used.remove(pos) # reset coordinate for use in other recursive calls above this stack frame
    return found

def solve(board):
    words = set()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            found = find_words(board, set(), '', (x, y)) # initialize empty set and prefix for first call
            words.update(found) # update set words with elements from set found
    return words


def make_board(letters=None):
    board = {}
    y = 0
    x = 0
    for letter in letters.split():
        board[x, y] = letter.lower()
        x += 1
        if x >= WIDTH:
            x = 0
            y += 1
    return board

def main():
    load_dictionary()


    import pprint
    # print PREFIXES
    pprint.pprint(PREFIXES)
    print DICTIONARY


    """
    prefixes =
    {'d': {'e': {'v': {'i': {'o': {'u': {'s': {}}}}}},
       'o': {'d': {'g': {'e': {}}}, 'g': {'g': {'e': {'d': {}, 'r': {}}}}}}}

    diciontary = set(['dodge', 'dogger', 'dogged', 'devious'])

    could probably also store prefixes in a trie
    """

    usage = """Usage: %prog [board_letters]

Example: %prog  T N N H A  I G N E I  S G E I B  C A H N I  O N F O E
python functional_programming_style_from_GitHub.py T N N H A  I G N E I  S G E I B  C A H N I  O N F O E


"""

    parser = optparse.OptionParser(usage=usage)
    options, args = parser.parse_args()

    if args:
        board = make_board(letters=' '.join(args))
    else:
        print 'invalid board input'

    # print_board(board)
    pprint.pprint(board)
    print '----'
    words = solve(board)
    total_score = 'x'
    for word in sorted(words):
        print word

    # print '----'
    # print 'Total score:', total_score, 'from', len(words), 'words'

if __name__ == '__main__':
    main()