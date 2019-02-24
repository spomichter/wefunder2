import random
import math

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

        self.main()

    def main(self):
        for x in range(17):
            self.players.append("player"+str(x))

        print(self.players)
        currentwinners = []
        r = 1
        while (len(currentwinners)) > 1:
            R = round(r, self.players)
            currentwinners = (R.run())



class round:
    players = []
    winners = []
    roundnum = 0
    def __init__(self,num, players):
        self.roundnum = num
        self.players = players


    def run(self):

        if self.power2(len(self.players)) == True:
            for i in range(0, len(self.players), 2):
                m = Match(self.players[i], self.players[i+1])
                self.winners.append(m.getWinner())

        else: #if not a power of two
            freepasses = self.floor_log(len(self.players))
            print(str(freepasses) + " players got a free pass")
            for i in range(freepasses):
                self.winners.append(self.players[i])
                self.players.pop(i)

            for i in range(0, len(self.players), 2):
                m = Match(self.players[i], self.players[i+1])
                self.winners.append(m.getWinner())

        return(self.winners)

    def power2(self, num):
        return num != 0 and ((num & (num - 1)) == 0)

    def floor_log(self,num):
        if num == 0:
            return 0
        return num - (2 ** int(math.log(num, 2)))



k = tournamentRunner()
#m = round(1, ['1324', 'asdf'])
#print(m.floor_log(11))





