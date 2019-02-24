import random
import math
import numpy
import smtplib, ssl
from playerinput import Frame

class Match:
    person1 = ''
    person2 = ''
    loser = 0
    rand = (random.uniform(0, 1))
    #print(rand)
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
        #for x in range(16):
            #self.players.append("player" + str(x))

        self.player = Frame.players #PLAYERS GOTTEN FROM playerinput.py

        print(self.players)
        players = self.players
        r = 1

        while (len(players)) >= 1:
            R = round(r, players)
            players = R.run(players)
            print("Winners for round " + str(r) + str(players))
            r+=1

            # Save to external file
            a = numpy.asarray(players)
            numpy.savetxt('rounds.csv', a, delimiter=",")

        print("FINAL WINNER: " + str(players))


    def sendMail(self,email):

        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = "pomichterstash@gmail.com"  # Enter your address
        receiver_email = email  # Enter receiver address
        #password = input("Type your password and press enter: ") # For typing in password
        password = "insert-your-password-here"
        message = """\
        Subject: CONGRATS!!!!!

        You won the Foosball Mania tournament!
        
        Thank you for coming"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)



class round:
    players = []
    winners = []
    roundnum = 0
    def __init__(self,num, players):
        self.roundnum = num
        self.players = players
        print("Round " + str(num))

    def run(self, winners):

        if self.power2(len(self.players)) == True:
            for i in range(0, len(self.players), 2):
                m = Match(self.players[i], self.players[i+1])
                winners.append(m.getWinner())
                print("stuck here")

        else: #if not a power of two
            freepasses = self.floor_log(len(self.players))
            print(str(freepasses) + " players got a free pass")
            for i in range(freepasses):
                self.winners.append(self.players[i])
                self.players.pop(i)

            for j in range(0, len(self.players), 2):
                m = Match(self.players[j], self.players[j+1])
                self.winners.append(m.getWinner())

        return(winners)

    def power2(self, num):
        return num != 0 and ((num & (num - 1)) == 0)

    def floor_log(self,num):
        if num == 0:
            return 0
        return num - (2 ** int(math.log(num, 2)))


k = tournamentRunner()
#m = round(1, ['1324', 'asdf'])
#print(m.floor_log(11))





