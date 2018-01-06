import time,random,sys,os

def print_slow(str, speed):
    """prints the text letter by letter"""
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)

def cls():
    """clears screen"""
    os.system('cls' if os.name=='nt' else 'clear')

def check_answer(self, question, answers):
    """checks to make sure the player is actually inputing a valid option"""
    answer = " "
    while answer not in answers:
        answer = input(question).lower()
    return answer
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Character():
    """Defines character attributes and actions"""

    def __init__(self, name, inventory = {}, hp = 100, ap = 10):
        """player attributes"""
        self.name = name
        self.hp = hp
        self.ap = ap
        self.inventory = inventory
        self.classed = None
        self.weapon = None

    #Combat Manager
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






