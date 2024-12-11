from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _create_deck(self):
        super()._create_deck()
        for joker in "1", "2":
            card = Card(f"JOKER-{joker}", f"JOKER-{joker}")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j.cards)
    print(j)
    for i in range(5):
        print(j.draw())
    print(j)
    print(f"{j = }")
