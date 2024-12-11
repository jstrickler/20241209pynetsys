import random
from card import Card

class CardDeck:
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
    SUITS = "Clubs Diamonds Hearts Spades".split()

    def __init__(self):
        self._create_deck()
    
    def _create_deck(self):
        self._cards = []  # empty list
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)    
    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __add__(self, other):
        temp_deck = CardDeck()
        temp_deck._cards = self._cards + other._cards
        return temp_deck

    def __len__(self):
        return len(self._cards)

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"
    
    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}:{len(self)}"

if __name__ == "__main__":
    d = CardDeck()
    print(f"{d = }")
    d.shuffle()
    print(f"{d.cards = }")
    for i in range(5):
        card = d.draw()
        print(card)
    print(d)
    print(f"{len(d) = }")
    
    d2 = CardDeck()
    d3 = d + d2
    print(d3)
