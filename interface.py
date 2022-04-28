import random
import dice
from player import Player
from effects import Effect

numPlayers = input("Enter the number of players: ")
players = []
for i in range(0,int(numPlayers)):
    players.append(Player([]))

random.shuffle(players)
for i in range(0,3):
    for player in players:
        print("Player ", player.id, ": pick die ", i)

        for index, d in enumerate(dice.allDice):
            print("[{}] - {}".format(index,d().name))

        selection = input("Select a die: ")
        player.dice.append(dice.allDice[int(selection)]())
    
for cur,n in zip(players,players[1:]+[players[0]]):
    cur.link(n)

print("The players and the order is as follows:")
for player in players:
    print("Player {}:".format(player.id),end=" ")
    for die in player.dice:
        print("{} ".format(die.name),end="")
        
    print("\n",end="")


while len([player for player in players if not player.permaDead]) > 1:
    for player in [player for player in players if not player.permaDead]:
        print("Player {} turn".format(player.id))
        player.setup()
        #basically rewrite roll to accept player input
        dicePool = [x for x in player.dice if not x.frozen]
        maxDice = 2
        if Effect.GROWTH in player.effects or Effect.SWARM in player.effects:
            maxDice = 3

        if len(dicePool) < maxDice:
            maxDice = len(dicePool)

        rollDice = []
        for i in range(0,maxDice):
            for index,die in enumerate(dicePool):
                print("[{}] - {}".format(index,die.name))
            choice = input("Pick a die:")
            rollDice.append(dicePool[int(choice)])
            dicePool.pop(int(choice))

        results = [x.roll() for x in rollDice]
        print("You got: ", end="")
        for result in results:
            print("{} ".format(result.name),end="")

        player.applyResults(results)
        player.cleanup()
        print()
        print("---------RESULTS-------------")
        for player in players:
            print("Player {} health: {}".format(player.id,player.health))
            print("Effects: ",end="")
            for effect in player.effects:
                print("{} ".format(effect),end="")
            print()
        print("-----------------------------")
