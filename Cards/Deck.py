class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
class Deck():
    def __init__(self):
        self.deck_list = self.generate_deck()

    def generate_deck(self):
        suits = ['spade', 'clubs', 'diamonds', 'hearts']
        values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        deck = []
        for suit in suits:
            for value in values:
                deck.append(Card(suit, value))
        return deck
        
    def shuffle_deck(self):
        pass