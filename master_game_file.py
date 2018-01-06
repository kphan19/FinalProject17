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

player = Character("Tom")

player.inventory["silver"]=2
player.inventory["gold"]=3

for k, v in player.inventory.items():
    print(k, ":", v).sort()




