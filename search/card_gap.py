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

# card_gap takes in the max possible card gap and returns the card_gap
def card_gap(m):
	


