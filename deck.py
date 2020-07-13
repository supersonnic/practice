import random
class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    cards = []
    def __init__(self):
        for suit in Card.suits:
            for value in Card.values:
                Deck.cards.append(Card(suit, value))
                Deck.count += 1

    def __repr__ (self):
        return "Deck of {} cards".format(Deck.count)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        deal = []
        num_cards = self.count()
        if num_cards == 0:
            raise ValueError("All cards have been dealt")
        for i in range(num):
            if Deck.count != 0:
                deal.append(Deck.cards.pop())
                Deck.count -= 1
        return deal

    def shuffle(self):
        num_cards = self.count()
        if num_cards != 52:
            raise ValueError("Only full decks can be shuffled")
        return random.shuffle(Deck.cards)

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, num):
        return self._deal(num)
