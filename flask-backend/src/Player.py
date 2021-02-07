from Card import Card, ranks, values

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def calculateCurrentScore(self):
        h = {}
        for card in self.hand:
            if card.isFlipped:
                if card.rank not in h:
                    h[card.rank] = [1,card.value]
                else:
                    h[card.rank][0] += 1

        score = 0
        for key,value in h.items():
            if value[0] == 1:
                score += value[1]
            elif value[0] > 1:
                while value[0] > 1:
                    value[0] = value[0] - 2
                if value[0] == 1:
                    score += value[1]
            else:
                raise "InvalidScoring"

        self.score = score
        print("Score: " + str(score))
        return score