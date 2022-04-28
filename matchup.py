from player import Player
import effects
import dice
import abilities
import random
class Results:
    def __init__(self,w=0,l=0,t=0):
        self.wins = w
        self.losses = l
        self.ties = t
        
    def addWin(self):
        self.wins += 1

    def addLoss(self):
        self.losses += 1

    def addTie(self):
        self.ties += 1

    def winPercent(self):
        return self.wins/(self.wins+self.losses+self.ties)*100

    def __add__(self,other):
        return Results(self.wins+other.wins,self.losses+other.losses,self.ties + other.ties)
    
class Matchup:
    def __init__(self,players,matches):
        self.players = {}
        self.matches = matches
        for player in players:
            self.players.update({player:Results()})
            
    def calcResults(self):
        for i in range(0,self.matches):
            self.game() #Run a game
            self.resetPlayers() #Reset players
        
    def showResults(self):
        for player,score in self.players.items():
            for d in player.dice:
                print("{} ".format(d.name),end="")
                
            print("\t{:<6} W\t{:<6} L\t{:<6} T\t{:.02f}% Win Rate".format(score.wins,score.losses,score.ties,score.winPercent()))


    def returnResults(self):
        return self.players

    def game(self):
        combatants = list(self.players.keys())
        random.shuffle(combatants)
        for cur,n in zip(combatants,combatants[1:]+[combatants[0]]):
            cur.link(n)
        turns = 0
        while len(combatants) > 1 and turns < 1000:
            for player in combatants:
                player.turn()
            for player in combatants:
                if player.permaDead:
                    self.players[player].addLoss()

            turns += 1
            combatants = [player for player in combatants if not player.permaDead]    

        if len(combatants) == 1:
            self.players[combatants[0]].addWin()
        else:
            for player in combatants:
                self.players[player].addTie()
        
    
    def resetPlayers(self):
        for player in self.players.keys():
            player.reset()

    def getPlayer(self,id):
        return list(self.players.keys())[id]

    
        


