"""
Card gap is defined as how many cards (of cardboard) stacked on an explosive such that the explosive 
will not explode when hit with a hammer. 
Find the card gap of an explosive. 
"""

card_gap = 6

def hammer(n):
	if n < card_gap:
		return True
	return False

# card_gap takes in the max possible card gap and returns the card gap number
def card_gap(m):
	start = 0 
	end = m
	while start <= end: 
		middle = (end - start)//2 + start
		if hammer(n): 
			start = middle + 1
		else: 
			end = middle - 1
	return start

# edge case
# start explodes, end does not. m = 1. Which means, start = 0, end = 1, middle = 0


