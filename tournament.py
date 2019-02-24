import random

class Match:
    person1 = ''
    person2 = ''
    loser = 0
    rand = (random.uniform(0, 1))
    print(rand)
    def __init__(self,p1, p2):
        self.person1 = p1
        self.person2 = p2
        print(self.getWinner() + " beat " + self.loser)

    def getWinner(self):
        if self.rand > 0.5:
            self.loser = self.person2
            return self.person1
        else:
            self.loser = self.person1
            return self.person2



class tournamentRunner:
    players = []
    def __init__(self):
        players = []
        self.main()

    def main(self):








