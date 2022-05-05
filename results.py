import multiprocessing as mp
import json

class Results:
    def __init__(self,manager):
        self.results = manager.dict()

    def addToResults(self,playerResults):
        #Convert {player1:Results(),player2:Results()} to {player1:{player2,Results()}}
        c = list(playerResults.items())
        if not c[0][0] in self.results:
            self.results[c[0][0]] = {}
        d = self.results[c[0][0]]
        d.update({c[1][0]:c[1][1]})
        self.results[c[0][0]] = d
        print("{},{}".format(len(self.results.values()),len(self.results.values()[-1])))
   
   
    #Not implemented yet.
    def readResults(self,filename):
        pass

    #Not actually implemented.
    #Gonna make this XML not CSV.
    #I lied, gonna make it JSON not XML
    def writeResults(self,filename):
        with open(filename,'w') as f:
            f.write('{"results":[\n')
            for player,versus in self.results.items():
                print(player)
                print(versus)
                f.write('\t{{ "id": {},\n'.format(player.id))
                f.write('\t"dice": [')
                for d in player.dice:
                    f.write('"{}"{}'.format(d.name,',' if d != player.dice[-1] else ''))
                f.write('],\n')
                f.write('\t"against": [\n')
                for p2,r in versus.items():
                    print(p2)
                    print(r)
                    f.write("\t\t{\n")
                    f.write('\t\t\t"versus":{},\n'.format(p2.id))
                    f.write('\t\t\t"wins":{},\n'.format(r.wins))
                    f.write('\t\t\t"losses":{},\n'.format(r.losses))
                    f.write('\t\t\t"ties":{}\n'.format(r.ties))
                    f.write("\t\t}}{}\n".format(',' if (p2,r) != list(versus.items())[-1] else ''))
                f.write("\t\t]\n")
                f.write("\t}}{}\n".format(',' if player != self.results.keys()[-1] else ''))
            f.write(']}\n')





     
    

