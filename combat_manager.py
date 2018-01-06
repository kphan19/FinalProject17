#For testing the combat manager
import random
# Combat Manager
def get_atk(self):
    """How much damage is delt"""
    atk = random.randint(4, self.ap)
    return atk
def take_dmg(self, dmg):
    """How much damage is taken"""
    self.hp = self.hp - dmg
def rnd_attack(self):
    """Randomizes a choice between attack and defend for attacker (CPU)"""
    atk = random.choice(["attack", "defend"])
    return atk
