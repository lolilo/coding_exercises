"""
Card gap is defined as how many cards (of cardboard) stacked on an explosive such that the explosive 
will not explode when hit with a hammer. 
Find the card gap of an explosive. 
"""

card_gap = 6

# given function. returns True if n < card_gap (explodes), returns False otherwise (does not explode)
def hammer(n):
	if n < card_gap:
		return True
	return False

# card_gap takes in the max possible card gap and returns the card gap number
def card_gap(m):
	start = 0 
	end = m
	while start <= end: # might be able to end with just start < end, if we assume max possible is > 0. 
		middle = (end - start)//2 + start # offset by start
		if hammer(middle): 
			start = middle + 1
		else: 
			end = middle - 1
	return start # make sure you understand why we return start and not end

# edge case
# consider a range of only length 2
# start = middle = 0, end = 1
# start explodes, end does not. m = 1//2 (+ start) = 0. 

