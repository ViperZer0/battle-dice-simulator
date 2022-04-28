from random import choice
from abilities import *

class Dice:
    def __init__(self):
        self.name = "X"
        self.abilities = []
        self.frozen = False
        self.meditating = False
    def roll(self):
        if not self.frozen:
            return choice(self.abilities)
        else:
            return None
    def __hash__(self):
        return self.name.lower()

    def __eq__(self,other):
        if type(other) == str:
            return self.name.lower() == other.lower()
        if type(other) == type(self):
            return self.name.lower() == other.name.lower()
        else:
            return False
   
class Fairy(Dice):
    def __init__(self):
        self.name = "Fairy"
        self.frozen = False
        self.meditating = False
        self.abilities = [Growth(), Growth(), Swarm(), Light(), Dark(), Focus()]


class Nymph(Dice):
    def __init__(self):
        self.name = "Nymph"
        self.frozen = False
        self.meditating = False
        self.abilities = [Growth(), Growth(), Water(), Light(), Light(), Drain()]


class Alien(Dice):
    def __init__(self):
        self.name = "Alien"
        self.frozen = False
        self.meditating = False
        self.abilities = [Swarm(), Swarm(), Fire(), Dark(), Ice(), Focus()]

class Zombie(Dice):
    def __init__(self):
        self.name = "Zombie"
        self.frozen = False
        self.meditating = False
        self.abilities = [Swarm(), Swarm(), Dark(), Dark(), Poison(), Curse()]

class Kraken(Dice):
    def __init__(self):
        self.name = "Kraken"
        self.frozen = False
        self.meditating = False
        self.abilities = [Water(), Water(), Shield(), Dark(), Poison(), Ice()]

class Mermaid(Dice):
    def __init__(self):
        self.name = "Mermaid"
        self.frozen = False
        self.meditating = False
        self.abilities = [Growth(), Water(), Water(), Light(), Lightning(), Lightning()]

class Phoenix(Dice):
    def __init__(self):
        self.name = "Phoenix"
        self.frozen = False
        self.meditating = False
        self.abilities = [Fire(), Fire(), Light(), Lightning(), Lightning(), Meditate(self)]

class Dragon(Dice):
    def __init__(self):
        self.name = "Dragon"
        self.frozen = False
        self.meditating = False
        self.abilities = [Fire(),Fire(),Bash(),Shield(),Focus(),Curse()]

class Knight(Dice):
    def __init__(self):
        self.name = "Knight"
        self.frozen = False
        self.meditating = False
        self.abilities = [Bash(),Bash(),Water(),Shield(),Light(),Ice()]

class Pirate(Dice):
    def __init__(self):
        self.name = "Pirate"
        self.frozen = False
        self.meditating = False
        self.abilities = [Swarm(),Water(),Fire(),Bash(),Bash(),Poison()]

class Tank(Dice):
    def __init__(self):
        self.name = "Tank"
        self.frozen = False
        self.meditating = False
        self.abilities = [Water(),Bash(),Shield(),Shield(),Light(),Meditate(self)]

class Robot(Dice):
    def __init__(self):
        self.name = "Robot"
        self.frozen = False
        self.meditating = False
        self.abilities = [Fire(),Shield(),Shield(),Lightning(),Lightning(),Focus()]

class Unicorn(Dice):
    def __init__(self):
        self.name = "Unicorn"
        self.frozen = False
        self.meditating = False
        self.abilities = [Growth(),Water(),Light(),Light(),Lightning(),Lightning()]

class Cleric(Dice):
    def __init__(self):
        self.name = "Cleric"
        self.frozen = False
        self.meditating = False
        self.abilities = [Water(),Fire(),Light(),Light(),Drain(),Meditate(self)]

class Puppet(Dice):
    def __init__(self):
        self.name = "Puppet"
        self.frozen = False
        self.meditating = False
        self.abilities = [Growth(),Fire(),Dark(),Dark(),Focus(),Curse()]

class Shadow(Dice):
    def __init__(self):
        self.name = "Shadow"
        self.frozen = False
        self.meditating = False
        self.abilities = [Swarm(),Dark(),Dark(),Poison(),Drain(),Curse()]

class Wizard(Dice):
    def __init__(self):
        self.name = "Wizard"
        self.frozen = False
        self.meditating = False
        self.abilities = [Water(),Fire(),Lightning(),Lightning(),Ice(),Focus()]

class Mage(Dice):
    def __init__(self):
        self.name = "Mage"
        self.frozen = False
        self.meditating = False
        self.abilities = [Light(),Dark(),Lightning(),Lightning(),Drain(),Meditate(self)]

class Echnida(Dice):
    def __init__(self):
        self.name = "Echnida"
        self.frozen = False
        self.meditating = False
        self.abilities = [Dark(),Poison(),Poison(),Focus(),Meditate(self),Curse()]

class Goblin(Dice):
    def __init__(self):
        self.name = "Goblin"
        self.frozen = False
        self.meditating = False
        self.abilities = [Swarm(),Fire(),Bash(),Dark(),Poison(),Poison()]

class Yeti(Dice):
    def __init__(self):
        self.name = "Yeti"
        self.frozen = False
        self.meditating = False
        self.abilities = [Growth(),Bash(),Ice(),Ice(),Drain(),Curse()]

class Troll(Dice):
    def __init__(self):
        self.name = "Troll"
        self.frozen = False
        self.meditating = False
        self.abilities = [Fire(),Bash(),Shield(),Poison(),Ice(),Ice()]

class Assassin(Dice):
    def __init__(self):
        self.name = "Assassin"
        self.frozen = False
        self.meditating = False
        self.abilities = [Bash(),Dark(),Dark(),Poison(),Focus(),Focus()]

class Elf(Dice):
    def __init__(self):
        self.name = "Elf"
        self.frozen = False
        self.meditating = False
        self.abilities = [Growth(),Fire(),Light(),Focus(),Focus(),Meditate(self)]

class Hero(Dice):
    def __init__(self):
        self.name = "Hero"
        self.frozen = False
        self.meditating = False
        self.abilities = [Water(),Light(),Light(),Drain(),Drain(),Meditate(self)]

class Vampire(Dice):
    def __init__(self):
        self.name = "Vampire"
        self.frozen = False
        self.meditating = False
        self.abilities = [Swarm(),Dark(),Drain(),Drain(),Meditate(self),Curse()]

class Monk(Dice):
    def __init__(self):
        self.name = "Monk"
        self.frozen = False
        self.meditating = False
        self.abilities = [Growth(),Water(),Fire(),Focus(),Meditate(self),Meditate(self)]

class Giant(Dice):
    def __init__(self):
        self.name = "Giant"
        self.frozen = False
        self.meditating = False
        self.abilities = [Bash(),Shield(),Ice(),Meditate(self),Meditate(self),Curse()]

class Cyclops(Dice):
    def __init__(self):
        self.name = "Cyclops"
        self.frozen = False
        self.meditating = False
        self.abilities = [Bash(),Lightning(),Lightning(),Ice(),Curse(),Curse()]

class Werewolf(Dice):
    def __init__(self):
        self.name = "Werewolf"
        self.frozen = False
        self.meditating = False
        self.abilities = [Swarm(),Dark(),Poison(),Meditate(self),Curse(),Curse()]

allDice = [Fairy,Nymph,Alien,Zombie,Kraken,Mermaid,Phoenix,Dragon,Knight,Pirate,Tank,Robot,Unicorn,Cleric,Puppet,Shadow,Wizard,Mage,Echnida,Goblin,Yeti,Troll,Assassin,Elf,Hero,Vampire,Monk,Giant,Cyclops,Werewolf]











