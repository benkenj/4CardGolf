from Player import Player
from Deck import Deck
from Card import Card, ranks, values, suits
class Game:
    def __init__(self, deck, players):
        self.currently_playing = False
        self.deck = deck
        self.players = players
        self.top_card = None
    
    def setup(self):
        pass

    def start(self):
        self.deal()
        self.setBoard()

        self.currently_playing = True
        
        for i in range(4):
            for player in self.players:
                self.takeTurn(player)

        cur_min = 100
        best_player = None
        for player in self.players:
            score = player.calculateCurrentScore()
            if cur_min > score:
                cur_min = score
                best_player = player
        print("###############")
        print("The Winner is: " + best_player.name)
        print("###############")

        currently_playing = False   

    def getLoser(self):
        pass

    def getGameState(self):
        pass

    def deal(self):
        for i in range(4):
            for player in self.players:
                # grab deck top card
                player.hand.append(self.deck.popTopCard())

        assert self.deck.getDeckCurrentSize() == (52-len(self.players)*4)

    def setBoard(self):
        self.setTopCard(self.deck.popTopCard())
        
    def setTopCard(self,card):
        print("New top card is: " + card.rank + " " + card.suit)
        self.top_card = card
    
    def getTopCard(self):
        return self.top_card

    def _isValid(self,card_to_play):
        return not card_to_play.isFlipped

    def takeTurn(self, player):
        #add turn type and card to play as parameters
        print(player.name + "'s Turn: ")
        assert self.getTopCard() != None
        print("Top card: " + self.getTopCard().rank + " " + self.getTopCard().suit)
        print("CurrentHand: ")
        for card in player.hand:
            flipped = "FLIPPED"
            if not card.isFlipped:
                flipped = "HIDDEN"

            print( card.rank + " " + card.suit + " | " + flipped)

        turn_type = "NONE"
        val = input("Options: F,T,D: ") 
        if val == "F":
            turn_type = "FLIP"
        elif val == "T":
            turn_type = "GRAB_TOP"
        elif val == "D":
            turn_type = "GRAB_DECK"
        else:
            raise "BadInput"
        card_to_play = None
        val = input("Card: 0,1,2,3: ") 

        if val != "0" and val != "1" and val != "2" and val != "3":
            raise "BadInput"
        if player.hand[int(val)].isFlipped:
            #TODO: retry
            raise "Implement retry on wrong card click"

        card_to_play = int(val)

        if not self._isValid(player.hand[card_to_play]):
            raise "Invalid turn"

        if turn_type == "FLIP":
            print(player.name  + " fliping")
            
        elif turn_type == "GRAB_TOP":
            print(player.name + " grabbing TOP")
            temp = player.hand[card_to_play]
            player.hand[card_to_play] = self.top_card

            self.top_card = temp
        elif turn_type == "GRAB_DECK":
            print(player.name + " grabbing DECK")
            self.top_card = player.hand[card_to_play]
            player.hand[card_to_play] = self.deck.popTopCard()
            
        else:
            raise "Unknown turn type"
        player.hand[card_to_play].flip()
        player.calculateCurrentScore()
        print(" ")

