class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):  # getter property 
        return self._rank
    # rank = property(rank)
    
    @property
    def suit(self):
        return self._suit
    
    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        # Card("8", "Diamonds")
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    # from card import Card
    c1 = Card("8", "Diamonds")
    c2 = Card("3", "Hearts")
    print(f"{c1.rank = }")
    print(f"{c2.suit = }")
    
    print(c1)   # str()
    print(f"{c1 = }")  # repr()
