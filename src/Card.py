ranks =['Ace','2','3','4','5','6','7','8','9','10','Jack',"Queen","King"]
values =[1,2,3,4,5,6,7,8,9,10,10,10,0]
suits = ['Heart','Diamond','Spade','Club']

class Card:
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.isFlipped = False
    
    def printCard(self):
        print( self.rank + " " + self.suit )

    def flip(self):
        if self.isFlipped:
            raise "Card already flipped"
        self.isFlipped = True        