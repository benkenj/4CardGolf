from DeckFactory import DeckFactory
from Game import Game
from Player import Player

if __name__ == "__main__":
    factory = DeckFactory()
    deck = factory.createShuffledDeck()
    players = []
    matt = Player("Matt")
    ben = Player("Ben")
    #quinn = Player("Quinn")
    #jay = Player("Jay")
    players.append(matt)
    players.append(ben)
    #players.append(quinn)
    #qplayers.append(jay)
    
    game = Game(deck,players)
    game.start()
