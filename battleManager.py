from matchup import Matchup
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

    """
    def duel(pool,players,results):
        def error(e):
            print("ERROR: ", e)
        battles = itertools.combinations(players,2)
        #Yeah we're not doing multiple iterations
        end = 5937750
        
        for i,b in enumerate(filter(lambda x: not x[0].sharesDicewith(x[1]),battles)): 
                           
            a = pool.apply_async(battle,args=(b,1000,i,end,),callback = lambda x: pairResults(results,x),error_callback=error)
    """
