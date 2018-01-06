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

    # COMBAT MANAGER
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

class Story():
    def __init__(self):
        self.intro()

    # MAIN MENU
    def intro(self):
        """Prints out a page displaying opening options"""
        print("#################################################################")
        print("#                                                               #")
        print("#            WELCOME TO THE GREAT KINGDOM OF AZURON             #")
        print("#                                                               #")
        print("#---------------------------------------------------------------#")
        print("#                                                               #")
        print("#                          - Play -                             #")
        print("#                          - Exit -                             #")
        print("#                          - Help -                             #")
        print("#                                                               #")
        print("#################################################################")
        self.intro_options()
    def intro_options(self):
        """Manages options for main menu"""
        choice = input(">>> ").lower()
        if choice == ("play"):
            """Clears screen and begins game"""
            cls()
            print_slow("Loading...", .09)
            time.sleep(2)
            cls()
            self.create_char()
        elif choice == ("exit"):
            """Exits the game"""
            print_slow("Goodbye.", .05)
            time.sleep(1)
            sys.exit()
        elif choice == ("help"):
            """Takes player to 'help' menu explaining game."""
            self.halp()
            time.sleep(1)
        else:
            """Loops in case player doesn't put in a valid option"""
            print_slow("Invalid input... Please try again\n", .04)
            self.intro_options()
    def halp(self):
        """Help menu explaining game and possible commands."""
        cls()
        print("#################################################################")
        print("#                                                               #")
        print("#                          HELP MENU                            #")
        print("#                                                               #")
        print("#---------------------------------------------------------------#")
        print("#                                                               #")
        print("# Welcome to the game. You are trapped in a mysterious castle   #")
        print("# and must find your way out. Collect items that will help you  #")
        print("# on your journey and battle your way to victory.               #")
        print("#                                                               #")
        print("# List of Commands:                                             #")
        print("# - *COMMANDS FOR PLAYER TO USE DONT FORGET TO UPDATE* to       #")
        print("#   navigate your way through the rooms of the castle           #")
        print("#                                                               #")
        print("# - 'examine' followed by an object to                          #")
        print("#   gain information about it                                   #")
        print("#                                                               #")
        print("# - 'take' followed by an item to add it to your                #")
        print("#   inventory                                                   #")
        print("#                                                               #")
        print("#         When you're ready, type 'menu' to return to           #")
        print("#                   the main title screen.                      #")
        print("#                                                               #")
        print("#################################################################")
        go_back = input(">>> ").lower()
        if go_back == ("menu"):
            """Takes player back to main menu and clears screen"""
            cls()
            self.intro()
        else:
            self.halp()

    # PLAYER SET UP
    def create_char(self):
        print("Still have to add in this part")



new_game = Story()
