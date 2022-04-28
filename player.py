from effects import Effect
import random
class Player:
    instances = 0
    def __init__(self,dice):
        self.id = Player.instances
        Player.instances += 1
        self.dice = []
        for d in dice:
            #instantiate dice object
            self.dice.append(d())
        self.target = None
        self.prev = None
        self.health = 10
        self.deaths = 0
        self.effects = []
        self.effectsQueue = []
        self.lightRolls = 0
        self.darkRolls = 0
        self.shieldHealth = 0
        self.permaDead = False
        self.dead = False
    def __hash__(self):
        return self.id

    def __eq__(self,other):
        return self.id == other.id
    
    #Player's turn.
    def turn(self):
        self.setup()
        self.applyResults(self.roll())
        self.cleanup()

    #Run at the beginning of the player's turn
    def setup(self):
        if self.isDead():
            self.deaths += 1
            self.dead = True
        try:
            freeze = random.sample(self.dice,self.effects.count(Effect.ICE))
        except ValueError:
            freeze = self.dice
        for die in freeze:
            die.frozen = True
        self.shieldHealth = 0


    #Handle player rolls, return results
    def roll(self):
        dicePool = [x for x in self.dice if not x.frozen] #Find all dice we can choose to roll
        maxDice = 2
        if Effect.GROWTH in self.effects or Effect.SWARM in self.effects:
            maxDice = 3

        if len(dicePool) < maxDice:
            maxDice = len(dicePool)

        rollDice = random.sample(dicePool,maxDice)
        results = [x.roll() for x in rollDice]
        return results 

    def applyResults(self,results):
        results.sort(key=lambda x: x.priority)
        for result in results:
            result.apply(self)

    
    #Run at the end of the player's turn
    def cleanup(self):
        lightCount = {0:0,1:1,2:4,3:10}
        darkCount = {0:0,1:1,2:5,3:13}
        self.target.damage(darkCount[self.darkRolls]*2**self.effects.count(Effect.FOCUS))
        self.target.damage(self.heal(lightCount[self.lightRolls]*2**self.effects.count(Effect.FOCUS)))
        self.darkRolls = 0
        self.lightRolls = 0
        #Clear currently applied effects, apply saved effects (shield and saved focus)
        self.effects.clear()
        self.effects = self.effectsQueue.copy()
        self.effectsQueue.clear()
        self.shieldHealth = 3*self.effects.count(Effect.SHIELD)
        for i in self.dice:
            i.frozen = False
            #Lil swaperooni here
            if i.meditating == True:
                i.frozen = True
                i.meditating = False
        if self.dead and self.health < self.deaths:
            self.permaDead = True
        else:
            self.dead = False
    #Return the healing "overcharge"
    def heal(self, amount):
        if Effect.POISON in self.effects:
            self.pureDamage(amount)
            return 0
        else:
            overcharge = (amount - (10 - self.health))
            if overcharge >= 0:
                self.health = 10
                return overcharge
            else:
                self.health += amount
                return 0
    #No poison damage (for CURSE)
    def pureHeal(self,amount):
        self.health += amount
        if self.health > 10:
            self.health = 10

    #return excess damage
    def reduceShield(self, amount):
        if amount < self.shieldHealth:
            self.shieldHealth -= amount
            return 0
        else:
            damage = amount - self.shieldHealth
            self.sheildHealth = 0
            return damage

    def damage(self, amount):
        if Effect.SHIELD in self.effects:
            self.pureDamage(self.reduceShield(amount))       
        else:
            self.pureDamage(amount)

    def pureDamage(self,amount):
        if amount > 0:
            self.health -= amount
            if self.health < 0:
                self.health = 0
                self.deaths += 1

    def isDead(self):
        if self.health == 0:
            return True
        else:
            return False
   
    
    def addEffect(self,effect):
        self.effects.append(effect)

    def addSavedEffect(self,effect):
        self.effectsQueue.append(effect)

    
    def link(self,target):
        self.target = target
        target.prev = self

    def reset(self):
        self.health = 10
        self.deaths = 0
        self.effects = []
        self.effectsQueue = []
        self.lightRolls = 0
        self.darkRolls = 0
        self.shieldHealth = 0
        self.permaDead = False
        self.dead = False
