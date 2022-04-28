import itertools
import dice
from player import Player
class PlayerManager():
    def __init__(self):
        combinations = itertools.combinations(dice.allDice,3)
        self.players = [Player(c) for c in combinations]
    
    def getPlayers(self):
        return self.players
   
    def selectPlayers(self,criteria):
        return [x for x in self.players if x.hasDice(criteria) or criteria == x]
    
    def selectPlayer(self,criteria):
        try:
            return self.selectPlayers(criteria)[0]
        except:
            return None


