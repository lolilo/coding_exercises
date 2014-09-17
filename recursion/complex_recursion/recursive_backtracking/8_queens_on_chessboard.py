
# http://stackoverflow.com/questions/5133509/eight-queens-problem-in-python
# http://pyeda.readthedocs.org/en/latest/queens.html

BOARD_SIZE = 8

def under_attack(column, existing_queens):
    # ASSUMES that row = len(existing_queens) + 1
    # this is hard coded into the algorithm. that's okay.
    row = len(existing_queens) + 1
    for queen in existing_queens:
        x,y = queen # get coordinates of existing queen
        if x == row: return True # check row
        if y == column: return True # check column
        if (column-y) == (row-x): return True # check left diagonal
        if (column-y) == -(row-x): return True # check right diagonal
    return False

# solve a board for n queens
def solve(n):
    if n == 0: 
        return [[]] # No RECURSION if n=0. 

    smaller_solutions = solve(n - 1) # RECURSION!!!!!!!!!!!!!!
    solutions = [] # list of tuples of coordinates of existing queens
    for solution in smaller_solutions: # I moved this around, so it makes more sense
        for column in range(0, BOARD_SIZE): # I changed this, so it makes more sense
            # try adding a new queen to row = n, column = column 
            if not under_attack(column, solution): 
                row = n - 1 # place queen as far to the left of the board as possible
                solutions.append(solution + [(row, column)])

    return solutions # list of list of tuples

if __name__ == "__main__":
    n = 2
    import pprint
    pprint.pprint(solve(n))
    print len(solve(n))
    # n = 8
    # print len(solve(n))
