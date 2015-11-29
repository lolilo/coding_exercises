class Card(object):
    # What information does a card contain?
        # suit and rank
    # What actions should a card have?
        # tell suit and rank

    def __init__(self, number):
        self.ranks = range(2, 11) + [J, Q, K, A]
        self.suits = [clubs, diamonds, hearts, spades]
        self.number = number

    def __str__(self):
        return "Card#" + str(self.number)

    # def __repr__(self):
    #     return "Card#" + str(self.number)
