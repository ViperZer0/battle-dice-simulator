import time
import random
import itertools
import multiprocessing as mp
import dice
import os
from player import Player
from matchup import Results
from matchup import Matchup

def combineResults(dict1,dict2):
    for player in dict2.keys():
        if player in dict1.keys():
            dict1[player] += dict2[player] #Add Results from dict2 to dict1
        else:
            dict1[player] = dict2[player] #otherwise instantiate
    return dict1
#For when dict2 is only a matchup of two players
def pairResults(dict1,dict2):
    #Convert {player1:Results(),player2:Results()} to {player1:{player2,Results()}}
    c = list(dict2.items())
    if not c[0][0] in dict1:
        dict1[c[0][0]] = {}
    d = dict1[c[0][0]]
    d.update({c[1][0]:c[1][1]})
    dict1[c[0][0]] = d
    print("{},{}".format(len(dict1.values()),len(dict1.values()[-1])))
    return dict1

def split_every(n,iterable):
    iterable = iter(iterable)
    yield from iter(lambda: list(itertools.islice(iterable, n)), [])

def indexOf(sResults,key):
    for index,sResults in enumerate(sResults):
        if sResults[0] == key:
            return index
    else:
        return None

def playerHasDice(player,die):
    l = [d.name for d in player.dice]
    return die in l

def battle(b,matches,index,end):
    print("{}/{}: {:.02f}%".format(index,end,index/end*100))
    for die in b[0].dice:
        print("{} ".format(die.name),end="")
    print("vs. ",end="")
    for die in b[1].dice:
        print("{} ".format(die.name),end="")
    print()
    matchup = Matchup(b,matches)
    matchup.calcResults()
    #print("---------------------------------------")
    #matchup.showResults()
    #print("---------------------------------------")
    return matchup.players


def checkResults(results,focus):
    sortedResults = sorted(results.items(),key=lambda x:x[1].winPercent(),reverse=True)
    print("--------------------------------")
    printMakeup(sortedResults,slice(10))
    printSlice(sortedResults,checkResults.prevSortedResults,slice(10))
    print("--------------------------------")
    ind = indexOf(sortedResults,focus)
    if ind != None:
        printSlice(sortedResults,checkResults.prevSortedResults,slice(ind-5,ind+5))
    print("--------------------------------")
    printMakeup(sortedResults,slice(-10,None))
    printSlice(sortedResults,checkResults.prevSortedResults,slice(-10,None))
    print("--------------------------------")
    checkResults.prevSortedResults = sortedResults.copy()

def printMakeup(sortedResults,slicer):
    print("Makeup: ",end="")
    makeup = {}
    #Holy shit this feels so unhinged. Count the number of times a die appears in the top 10.
    for d in dice.allDice:
        for player in sortedResults[slicer]:
            if playerHasDice(player[0],d().name):
                if d().name in makeup:
                    makeup[d().name] = makeup[d().name] + 1
                else:
                    makeup[d().name] = 1
    makeupSort=sorted(makeup.items(),key=lambda x: x[1],reverse=True)
    for dName,count in makeupSort:
        print("{} {}/10\t".format(dName,count),end="")

    print()
    
def printSlice(sortedResults,prevSortedResults,slicer):
    for player,score in sortedResults[slicer]:
        #print("{}\t{}\tPlayer {}:".format(player,player in players,player.id),end="")
        for d in player.dice:
            print("{:<10} ".format(d.name),end="")
        print("\t{:<6} W\t{:<6} L\t{:<6} T\t{:.02f}% Win Rate\t".format(score.wins,score.losses,score.ties,score.winPercent()),end="")
        if prevSortedResults == {} or indexOf(prevSortedResults,player) == None:
            print("--")
        else:
            #How has the rank changed?
            print("{:+}".format(indexOf(prevSortedResults,player)-indexOf(sortedResults,player)))
    
    
def printDice(player):
    for d in player.dice:
        print("{} ".format(d.name),end="")
    print()

def selectPlayers(r,criteria):
    def hasDice(player,criteria):
        for crit in criteria:
            if not playerHasDice(player,crit):
                return False
        else:
            return True
        
    return [x for x in r if hasDice(x,criteria)]

def playersShareDice(p1,p2):
    for d in p1.dice:
        if d in p2.dice:
            return True
    else:
        return False
    
def findPlayer(players,dice):
    for player in players:
        for d in player.dice:
            if not d.name in dice:
                break
        else:
            return player
    return None

def readResults(players,results,filename):
    if os.path.isfile(filename):
        with open(filename,'r') as f:
            for line in f.readlines():
                items = line.strip().split(',')
                p = findPlayer(players,[items[0],items[1],items[2]])
                results.update({p:Results(int(items[3]),int(items[4]),int(items[5]))})
                
            
def writeResults(results,filename):
    #Save results
        with open(filename,'w') as f:
            for player,score in results.items():
                for d in player.dice:
                    f.write("{},".format(d.name))
                f.write("{},{},{}\n".format(score.wins,score.losses,score.ties))

def writePairResults(players,results,filename):
    with open(filename,'w') as f:
        #HEADER
        f.write("X,")#Blank cell
        for p2 in players:
            f.write("{} {} {} wins,".format(p2.dice[0].name,p2.dice[1].name,p2.dice[2].name))
            f.write("{} {} {} losses,".format(p2.dice[0].name,p2.dice[1].name,p2.dice[2].name))
            f.write("{} {} {} ties,".format(p2.dice[0].name,p2.dice[1].name,p2.dice[2].name))
        f.write("\n")
        #Rows
        for p in players:
            f.write("{} {} {},".format(p.dice[0].name,p.dice[1].name,p.dice[2].name))
            for p2 in players:
                if p == p2:
                    f.write("-,-,-,")
                else:
                    if p in results.keys() and p2 in results[p]:
                        #FLIP losses and wins, so table is read left to right, with the ROW winning against the COLUMN
                        f.write("{},{},{},".format(results[p][p2].losses,results[p][p2].wins,results[p][p2].ties))
                    elif p2 in results.keys() and p in results[p2]:
                        #This one is written normally!
                        f.write("{},{},{},".format(results[p2][p].wins,results[p2][p].losses,results[p2][p].ties))
                    else:
                        f.write("-,-,-,")
            f.write("\n")
      
            
def simulate(pool,players,results):
    #battles = itertools.combinations(players,4) #All possible combinations of players
    readResults(players,results,"results.csv")
    def addToResults(x):
        results = combineResults(results,x)
    while True:    
        for player in players:
            b = [player]
            b += random.sample(players,3)
                         
            a = pool.apply(battle,args=(b,1000,),callback = addToResults)

        while not a.ready():
            print("ITERATION #{}".format(iterations))
            checkResults()
            checkLowResults()
            writeResults(results,"results.csv")
            time.sleep(30)

        iterations += 1

def generateFileName(player):
    return ''.join([d.name for d in player.dice]) + '.txt'

def duel(pool,players,results):
    def error(e):
        print("ERROR: ", e)
    battles = itertools.combinations(players,2)
    #Yeah we're not doing multiple iterations
    end = 5937750
    
    for i,b in enumerate(filter(lambda x: not playersShareDice(x[0],x[1]),battles)): 
                       
        a = pool.apply_async(battle,args=(b,1000,i,end,),callback = lambda x: pairResults(results,x),error_callback=error)
    
    while not a.ready():
        time.sleep(60)
        writePairResults(players,results,"results.csv")
    if a.successful():
        print("Done!")
        writePairResults(players,results,"results.csv")
    else:
        print("Oh lord something went wrong. I am so sorry.")

            
def fightWinner(pool,players,results):
    winner = selectPlayers(players,["Yeti","Troll","Alien"])[0]
    players.remove(winner)
    iterations = 0

    def error(e):
        print("ERROR: ", e)
    while True:    
        for player in players:
            b = [player,winner]
            a = pool.apply_async(battle,args=(b,1000),callback = lambda x: combineResults(results,x),error_callback=error)

        while not a.ready():
            print("ITERATION #{}".format(iterations))
            checkResults(results,"results.csv")
            writeResults(results,"results.csv")
            time.sleep(60)
        iterations += 1

if __name__ == "__main__":
    checkResults.prevSortedResults = {} #Initialize global (whoops!)
    print("Starting...")
    combinations = itertools.combinations(dice.allDice,3)
    players = [Player(c) for c in combinations]

    #TOP RESULT: Mermaid Tank Hero.

    with mp.Pool(processes=4) as pool:
        manager = mp.Manager()
        results = manager.dict()
        #readResults(players,results)
        #simulate(players,results)
        #fightWinner(pool,players,results)
        duel(pool,players,results)
