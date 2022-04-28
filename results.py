import multiprocessing as mp
import json

class Results:
    def __init__(self):
        self.manager = mp.Manager()
        self.results = manager.dict()

    def addToResults(playerResults):
        #Convert {player1:Results(),player2:Results()} to {player1:{player2,Results()}}
        c = list(playerResults.items())
        if not c[0][0] in self.results:
            self.results[c[0][0]] = {}
        d = self.results[c[0][0]]
        d.update({c[1][0]:c[1][1]})
        self.results[c[0][0]] = d
        print("{},{}".format(len(self.results.values()),len(self.results.values()[-1])))
   
   
    #Not implemented yet.
    def readResults(filename):
        pass

    #Not actually implemented.
    #Gonna make this XML not CSV.
    def writeResults(filename):
        with open(filename,'w') as f:
            f.write(json.dumps(self.results))
     
    

