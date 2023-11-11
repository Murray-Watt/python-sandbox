# This code demonstrates some of the special methods in Python
# Special methods are always surrounded by double underscores and
# are used to implement functionality that is not directly
# accessible through normal syntax.
#
# For example, the __init__ method is called when an object is
# created and is used to initialize the object.
#
# The __len__ method is called when the built-in len() function is
# called on an object.
#
# The __getitem__ method is called when [] operator is called on an object
# (e.g. my_object[0]).
#


import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
