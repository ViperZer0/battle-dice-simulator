from matchup import Matchup
from results import Results
from multiprocessing import Pool
import itertools
class BattleManager():
    def __init__(self,playerManager):
        self.pm = playerManager
        self.battles = 1000

    def battle(self,name1,name2):
        p1 = self.pm.selectPlayer(name1)
        p2 = self.pm.selectPlayer(name2)
        matchup = Matchup([p1,p2],self.battles)
        matchup.calcScores()
        matchup.showScores()
        return matchup.returnScores()
    
    def runAllBattles(self):
        with Pool() as pool:
            results = Results()
            battles = itertools.combinations(self.pm.getPlayers(),2)
            #total combinations
            end = 5937750

            for i,b in enumerate(filter(lambda x: not x[0].sharesDiceWith(x[1]),battles)):
                a = pool.apply_async(battle,args=(b[0],b[1]),callback = results.addToResults,error_callback=lambda e: print("ERROR: {}".format(e)))

            a.wait()
            results.writeResults("results.xml")
