from Card import Card, ranks, values, suits
from Deck import Deck

class DeckFactory:
    def createShuffledDeck(self):
        cards = []
        for suit in suits:
            for i in range(len(ranks)):

                card = Card(suit, ranks[i], values[i])
                cards.append(card)
        
        deck = Deck(cards)
        deck.shuffle()
        return deck