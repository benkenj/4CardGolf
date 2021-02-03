from Card import Card
from random import sample

class Deck:
    def __init__(self,cards):
        self.cards = cards

    def shuffle(self):
        self.cards = sample(self.cards,len(self.cards))

    def getTopCard(self):
        return self.cards[-1]

    def popTopCard(self):
        return self.cards.pop()

    def getDeckCurrentSize(self):
        return len(self.cards)