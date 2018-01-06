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

def check_answer(question, answers):
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
        self.new_game()

    def new_game(self):
        global archer,mage,thief,brute #is there a way to not use global?
        """Set class values to 0 for class sorting quiz"""
        archer = 0
        mage = 0
        thief = 0
        brute = 0
        self.intro()
        cls()
        self.create_char()
        print_slow("\nThe story will now begin", .05)
        time.sleep(2)
        cls()
        print_slow("Loading...", .09)
        time.sleep(5)
        cls()
        self.start()

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

        global rndm_class
        rndm_class = 0
        print_slow("Please choose a name, adventurer. ", .03)
        time.sleep(1)
        name = input("\nName: ")
        player = Character(name)
        print_slow(f"Hello {name}.\n", .03)
        time.sleep(1)
        print_slow("Now we will set up your character.\n", .03)
        time.sleep(1)
        print_slow("Would you like to take a short quiz to assign your character a class?\n", .03)
        print_slow("If not, you will be assigned a random one.\n", .03)
        answer = check_answer("Yes or No?: ", ["yes", "no", "y", "n"])
        if answer == "yes" or answer == "y":
            time.sleep(1)
            cls()
            print_slow("Loading questions...", .09)
            time.sleep(3)
            cls()
            self.char_class_quiz()
        else:
            character_class = ["archer", "mage", "thief", "brute"]
            rndm_class = random.choice(character_class)
            self.chosen_class()
    def clsspts(self):
        global archer,mage,thief,brute
        answer = check_answer("Answer:  ", ["a", "b", "c", "d"])
        if answer == "a":
            archer += 1
            return archer
        if answer == "b":
            mage += 1
            return mage
        if answer == "c":
            thief += 1
            return thief
        if answer == "d":
            brute += 1
            return brute
    def char_class_quiz(self):
        print_slow("All questions will be multiple choice. Simply type the letter that corresponds to your answer.", .05)
        time.sleep(2)
        cls()
        print_slow("1) When you wake up in the morning, which of the following are you most likely to do?\na. Read a book\nb. Yoga\nc. Check your pockets\nd. Exercise\n\n", .02)
        self.clsspts()
        cls()
        print_slow("2) What are you most likely to do in a heated situation?\na. Keep your distance\nb. Try to calm everyone down\nc. Weasel your way out of it by lying\nd. Break something(like a person's face maybe)\n\n", .02)
        self.clsspts()
        cls()
        print_slow("3) Some of the most important things to you in life are...\na. patience, focus, and contemplation\nb. discipline, art, and spirit\nc. knowledge, mastery, and wealth\nd. challenge, health, and rivalry\n\n", .02)
        self.clsspts()
        cls()
        print_slow("4) If you were an animal, you would be a...\na. hawk\nb. dolphin\nc. cat\nd. shark\n\n", .02)
        self.clsspts()
        cls()
        print_slow("5) At a bar with friends, you are likely to be the...\na. sober one who watches over the others\nb. emotional rollercoaster\nc. one doin your own thing\nd. entertainer \n\n", .02)
        self.clsspts()
        cls()
        print_slow("6) Others might describe you as...\na. serious but kind\nb. different...in a good way;)\nc. sleek and thoughtful\nd. flashy and fun\n\n", .02)
        self.clsspts()
        cls()
        print_slow("7) Your idea of the perfect date would be...\na. going on a scenic hike\nb. going on a long walk on the beach with a good conversationalist\nc. I don't do dates...#night in with my pets\nd. dancing with an awesome partner at a huge party\n\n", .02)
        self.clsspts()
        cls()
        self.chosen_class()

    def chosen_class(self):
        if archer > mage and archer > thief and archer > brute or rndm_class == ("archer"):
            character_class = archer
            print_slow("Congratulations. You have been classified as an 'Archer'\n", .03)
            time.sleep(2)
            print_slow("You will be given certain advantages based on your class.", .03)
        elif mage > archer and mage > thief and mage > brute or rndm_class == ("mage"):
            character_class = mage
            print_slow("Congratulations. You have been classified as a 'Mage'\n", .03)
            time.sleep(2)
            print_slow("You will be given certain advantages based on your class.", .03)
        elif thief > archer and thief > mage and thief > brute or rndm_class == ("thief"):
            character_class = thief
            print_slow("Congratulations. You have been classified as a 'Thief'\n", .03)
            time.sleep(2)
            print_slow("You will be given certain advantages based on your class.", .03)
        elif brute > archer and brute > mage and brute > thief or rndm_class == ("brute"):
            character_class = brute
            print_slow("Congratulations. You have been classified as a 'Brute'\n", .03)
            time.sleep(2)
            print_slow("You will be given certain advantages based on your class.", .03)
        else:
            print_slow("You seem to have aspects of all the classes. You have the priviledge of choosing your class.\n", .03)
            time.sleep(2)
            print_slow("Your choices are: archer, mage, thief, or brute", .03)
            time.sleep(1)
            character_class = self.check_answer("\nClass: ", ["archer", "mage", "thief", "brute"])
            print_slow(f"Congratulations. You have selected to join the {character_class} class.\n", .03)
            time.sleep(2)
            print_slow("You will be given certain advantages based on your class.", .03)
            time.sleep(2)

    # ROOM1 / BEGINNING OF STORY
    def start(self):
        print("Still have to add in shtuff")



new_game = Story()
