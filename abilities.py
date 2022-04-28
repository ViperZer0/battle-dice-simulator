from effects import Effect
from enum import Enum
import random
#RESOLUTION ORDER:
#FOCUS (possibly double damage on every other ability)
#--STATUS EFFECTS--
#POISON 
#ICE
#SHIELD
#--DAMAGE--
#DARK
#FIRE
#BASH
#CURSE
#LIGHTNING
#DRAIN
#SWARM
#--HEAL--
#WATER
#GROWTH
#MEDITATE
#LIGHT (Always save for last!)
    

class Ability:
    def __init__(self):
        self.priority = 0
        self.name = ""
    def apply(self,caster,target):
        pass

class Focus(Ability):
    def __init__(self):
        self.priority = 1
        self.name = "Focus"
        self.saveChance = 0.5

    def apply(self,caster):
        if random.random() > self.saveChance:
            caster.addEffect(Effect.FOCUS)
        else:
            caster.addSavedEffect(Effect.FOCUS)

class Poison(Ability):
    def __init__(self):
        self.priority = 2
        self.name = "Poison" 

    def apply(self,caster):
        caster.target.addEffect(Effect.POISON)

class Ice(Ability):
    def __init__(self):
        self.priority = 3
        self.applyToNextChance = 0.15
        self.name = "Ice"

    def apply(self,caster):
        caster.target.damage(1*2**caster.effects.count(Effect.FOCUS))
        if random.random() < self.applyToNextChance:
            caster.target.addEffect(Effect.ICE)
        else:
            caster.prev.addEffect(Effect.ICE)

class Shield(Ability):
    def __init__(self):
        self.priority = 4
        self.name = "Shield" 
    def apply(self,caster):
        caster.addSavedEffect(Effect.SHIELD)

class Dark(Ability):
    def __init__(self):
        self.priority = 5
        self.name = "Dark"
        
    def apply(self,caster):
        caster.darkRolls += 1

class Fire(Ability):
    def __init__(self):
        self.priority = 6
        self.name = "Fire"

    def apply(self,caster):
        caster.target.pureDamage(2*2**caster.effects.count(Effect.FOCUS))

class Bash(Ability):
    def __init__(self):
        self.priority = 7
        self.name = "Bash"

    def apply(self,caster):
        #Is the target under any effects?
        if len(caster.target.effects) > 0:
            caster.target.damage(3*2**caster.effects.count(Effect.FOCUS))
        else:
            caster.target.damage(1*2**caster.effects.count(Effect.FOCUS))

class Curse(Ability):
    def __init__(self):
        self.priority = 8
        self.name = "Curse"

    def apply(self,caster):
        caster.target.damage(3*2**caster.effects.count(Effect.FOCUS))
        if Effect.POISON in caster.effects:
            caster.pureHeal(1)
        else:
            caster.pureDamage(1)

class Lightning(Ability):
    def __init__(self):
        self.priority = 9
        self.name = "Lightning"

    def apply(self,caster):
        #Fortunately for us every die with lightning on it has a 1/3 chance of being rolled
        caster.target.damage(1*2**caster.effects.count(Effect.FOCUS))
        roll = random.randint(0,2)
        while roll == 0:
            caster.target.damage(1*2**caster.effects.count(Effect.FOCUS))
            roll = random.randint(0,2)

class Drain(Ability):
    def __init__(self):
        self.priority = 10
        self.addDamageChance = 0.5
        self.name = "Drain"

    def apply(self,caster):
        healAmount = 1
        damageAmount = 1

        for i in range(0,caster.effects.count(Effect.FOCUS)):
            healAmount *= 2
            damageAmount *= 2
            if random.random() < self.addDamageChance:
                damageAmount += 1
            else:
                healAmount += 1

        caster.target.damage(damageAmount)
        caster.heal(healAmount)

class Swarm(Ability):
    def __init__(self):
        self.priority = 11
        self.name = "Swarm"

    def apply(self,caster):
        caster.addSavedEffect(Effect.SWARM)
        caster.target.damage(1*2**caster.effects.count(Effect.FOCUS))

class Water(Ability):
    def __init__(self):
        self.priority = 12
        self.name = "Water"

    def apply(self,caster):
        if caster.health == 0:
            caster.heal(3*2**caster.effects.count(Effect.FOCUS))
        else:
            caster.heal(2*2**caster.effects.count(Effect.FOCUS))

class Growth(Ability):
    def __init__(self):
        self.priority = 13
        self.name = "Growth"

    def apply(self,caster):
        caster.addSavedEffect(Effect.GROWTH)
        caster.heal(1*2**caster.effects.count(Effect.FOCUS))

class Meditate(Ability):
    def __init__(self,dice):
        self.priority = 14
        self.dice = dice
        self.name = "Meditate"

    def apply(self,caster):
        if caster.health < 6 and Effect.MEDITATE not in caster.effects: #don't use unless at less than max. Simplistic but...
            caster.heal(4*2**caster.effects.count(Effect.FOCUS))
            caster.addSavedEffect(Effect.MEDITATE)
            self.dice.meditating = True
         
class Light(Ability):
    def __init__(self):
        self.priority = 15
        self.name = "Light"

    def apply(self,caster):
        caster.lightRolls += 1
