import numpy as np
import random

K = 32.

def ELORating(winner, loser):
    Rw = np.power(10, (winner.rank/400.))
    Rl = np.power(10, (loser.rank/400.))
    Ew = Rw / (Rl + Rw)
    El = Rl / (Rl + Rw)

    newRw = winner.rank + K * (1 - Ew)
    newRl = loser.rank + K * (0 - El)

    winner.update_rating(newRw)
    loser.update_rating(newRl)



class Entry:
    '''
    Each entry is represented by the Entry class
    '''
    def __init__(self, title):
        self.title = title
        self.rank = 1000.0
        self.match = 0

    def __str__(self):
        return self.title + ' : ' + str(self.rank)

    def update_match(self):
        self.match += 1

    def update_rating(self, rating):
        self.rank = rating

class Match:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.select_winner()

    def select_winner(self):
        print ('Entry:\n1. {}\n2. {}').format(self.players[0], self.players[1])
        print('select winner [ 1 or 2 ]')
        x = raw_input()
        while (x != '1' and x != '2'):
            print ('select 1 or 2')
            x = raw_input()

        w = int(x)-1
        l = 1-w

        ELORating(self.players[w], self.players[l])

        print self.players[0].rank
        print self.players[1].rank

class DataBase:

    def __init__(self):
        self.data = []

    def addEntry(self, entry):
        self.data.append(entry)

    def sort(self):
        self.data.sort(lambda x, y: int(y.rank - x.rank))

    def printN(self,n):
        self.sort()
        if n > len(self.data):
            n = len(self.data)
        for i in range(n):
            print self.data[i]

    def matching(self):
        matching = []
        for i in range(len(self.data)):
            for j in range(i+1, len(self.data)):
                matching.append((i,j))
        matching = set(matching)

        for player1, player2 in matching:

            Match(self.data[player1], self.data[player2])


        self.printN(len(self.data))

if __name__ == '__main__':
    db = DataBase()
    db.addEntry(Entry('phantom menace'))
    db.addEntry(Entry('clone wars'))
    db.addEntry(Entry('revenge of sith'))
    db.addEntry(Entry('new hope'))
    db.addEntry(Entry('empire strikes back'))
    db.addEntry(Entry('return of jedi'))
    db.addEntry(Entry('force awakenes'))
    db.addEntry(Entry('rogue one'))

    db.matching()
