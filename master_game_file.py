import time,random,sys,os

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# MAINTENCANCE FUNCTIONS
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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# ROOM DEFINITIONS
location = 1
rooms = {
    1 :{"name":"Start",
        "description":"You wake up on a cold floor. Don't ask me how you got there. You sit up and decide to take a look around and take in your surroundings.\nCovering the floor across from you is a dusty ol' rug. The walls are tall and made of stone. On one of them, there is an unsettling painting \nof some random old lady. Opposite the painting is a small window. In the corner you spy a chest. Standing up, you check your pockets and find:\n1 gold\n1 silver\n10 copper\nand a crumpled up note...\n\nThe note reads:\n\"WELCOME TO THE ONCE GREAT KINGDOM OF AZURON. SO SORRY ABOUT YOUR CURRENT SITUATION BUT IT COULDN'T BE HELPED.\nYOUR OVERALL GOAL IS TO ESCAPE THIS CASTLE IN ONE PIECE (PREFERABLY ALIVE), HOWEVER THERE ARE MANY OTHER THINGS TO DO WHILE YOU'RE HERE.\nTHIS ROOM WILL SERVE AS YOUR TUTORIAL. I WISH YOU THE BEST OF LUCK.\"\n\n***REMINDER: If you ever get stuck type 'help' to access the help menu. It will give you a list of possible commands.\n\nTry using 'examine chest'.\n",
        "examine":{"door":{"nexamined":"\nOf course you would try the door. Unfortunately, it's locked up and barred nice and tight. No getting through there m8.\n"},
                   "window":{"nexamined":"\nYou peek your head out the window and realize that if you jump out, you'd end up being very, very dead.\nThe room you're in seems to be in some high up tower. There aren't any vines within arms reach that you could use to shimmy down the side either.\nWhat a shame.\n"},
                   "wall":{"nexamined":"\nYou look closely at the wall, hoping for some kind of clue as to what you're doing. You see nothing but tiny tally marks...alot of them.\n"},
                   "rug":{"nexamined":"\nThe rug looks expensive. As you go to take a look at it, something rattles...You flip it up and find...SHOCKER a trapdoor.\n"},
                   "painting":{"nexamined":"\nYou look at the old painting. Its eyes are so serious. It seems to be looking at something. You follow its gaze to the corner and see\na stick of some sort in the corner. Try using the \"get\" command. (\"get\" followed by item so \"get stick\")\n"},
                   "chest":""},
        "examine2":{"door":"\nYou already checked the door. You're still not getting out that way. Try something else.\n",
                    "window":"\nYou can't leave via the window. Nothing's changed about that. Try something else.\n",
                    "wall":"\nDo you really find the wall that interesting? My guy do something else.\n",
                    "rug":"\nThe rug is flipped up just like you left it, exposing that lovely trapdoor. Nothing else you can do with it though... Try something else.\n",
                    "trapdoor":"\nThe door is wide open. Go on down if you're done with this room.\n",
                    "painting":"\nAfter the stick, this lovely painting has no more significance. Find something else to do.\n"},
        "items":{"stick":"ntaken"},
        "opponents":{""}},
    2 :{"name":"Dining Hall",
        "description":"\nYou stumble through a heavy pair of doors into what appears to be a Dining Hall. You look around and see a large table in the center of the room,\na large tapestry on the west wall, a chest in the corner, and doors on the northern and eastern walls.\n",
        "north":6,
        "east":7,
        "examine":{"table":{"nexamined":"\nYou walk over to the table and see an arrow stuck on the tablecloth.\n"},
                   "tapestry":{"nexamined":"\nThere's a slight breeze coming from...behind the fabric? You give the tapestry a tug and the whole thing falls down\ncausing a cloud of dust to explode in your face. When the dust settles, you find another set of doors!\n"},
                   "chest":{"nexamined":"\nYou go to open the chest hoping to find something useful. Instead, when you lift the lid, a tiny little dart shoots out at you\nand gets you in the arm...how unfortunate. Luckily it didn't do too much damage, but in the future be cautious of possible traps.\n"},
                   "door":{"nexamined":"\nUse 'go' followed by a direction (north,west,east,south,up,down) to go through a door.\n"}},
        "examine2":{"table":"\nAfter the arrow, the table has no more significance. Find something else to do.\n",
                    "tapestry":"\nYou pulled it off already. Congrats. Try to do something else, like go through the doors? That is, if you're ready.\n",
                    "chest":"\nDo you want to get hit again? There's nothing more to this chest if you already learned your lesson. Try to do something else.\n",
                    "door":"\nIf you really need help with this, type 'help'.\n"},
        "items":{"arrow":"ntaken"},
        "opponents":{""}},
    7 :{"name":"Kitchen", # This was originally room 3 (Kitchen) but it leads to room 7 (dungeon) so i just got rid of a room description for 3
        "description":"\nYou open the door to what seems to be a kitchen. As you step in...oh dear. The floor gives way under you and you fall...\nYou end up losing some health. When your eyes adjust to the dim lighting, you see that you are in some kind of dungeon and face to face with..a MoNsTeR! Gasp.\n",
        "examine":"",
        "opponents":{"alive":["monster1"]},
        "items":{"spoon":"ntaken"}},
    4 :{"name":"Library",
        "description":"\nYou push on the doors. The light streaming in through the window in front of you is almost blinding. Once you're eyes adjust, \nyou realize you seem to be in some old library with a large, dusty shelf lining the wall.\n",
        "north":6,
        "east":2,
        "west":5,
        "examine":{"window":{"nexamined":"\nYou walk over to the west wall, in front of the giant set of windows, and give it a push. Surprisingly, it swings open with ease.\nOutside you see a huge yard. You could probably climb through the window if you tried...\n"},
                   "shelf":{"nexamined":"\nYou swipe your finger along the shelf and disrupt a very thick layer of dust. Then you notice a book sitting all by itself in the corner.\n"},
                   "book":{"nexamined":"\nOpening the book, you make the mistake of flipping through the pages revealing...more dust. Good job.\n"}},
        "examine2":{"window":"\nThe window is already open. You can go out if you want, or try doing something else.\n",
                    "shelf":"\nAfter the book, the shelf has no other significance, other than the fact that it's REALLY dusty. Try doing something else.\n",
                    "book":"\nDid you take it? If you didn't, you can if you want to. Otherwise Find something else to do.\n"},
        "items":{"book":"ntaken"},
        "opponents":{""}},
    5 :{"name":"Courtyard",
        "description":"\nHECK YEA BABY! FREE AT...last? Ha no, not that easy. You look around and notice the entire yard is surrounded by very large, concrete walls.\nToo bad, so sad. Off to the side, you see a piece of rope.\n",
        "east":4,
        "examine":{"wall":{"nexamined":"\nUnfortunately, the wall is too tall for you to climb, even with a rope. There is no hope of escape. Just give up.\n"},
                   "rope":{"nexamined":"\nIt's a decent length of rope. Could be useful later on.\n"}},
        "examine2":{"wall":"\nMan, you're not getting out that way. Trust me. I designed it that way. Find something else to do.\n",
                    "rope":"\nDid you take it? If you didn't, you can if you want to. Otherwise do something else.\n"},
        "items":{"rope":"ntaken"},
        "opponents":{""}},
    6 :{"name":"Ballroom",
        "description":"\nOoo. A spooky ballroom. There's barely any light coming into the room, making it extra spooky, and for good reason. DA DA!\nYour first monster has appeared!\n",
        "opponents":{"alive":["monster1"]}}}

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ALL ATTRIBUTES OF ANY CHARACTERS IN GAME
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

    # ROOMS AND STORY
    # Keeps screen neat by clearing previous commands
    def resetscreen(self):
        cls()
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print(rooms[location]["name"].upper())
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print(rooms[location]["description"])
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")

    def check_path(self):
        if "examined" in rooms[1]["examine"]["rug"] and "trapdoor" in rooms[1]["examine"] and "examined" in rooms[1]["examine"]["trapdoor"]:
            rooms[1]["down"] = 2

        elif "examined" in rooms[1]["examine"]["rug"]:
            rooms[1]["examine"]["trapdoor"] = {"nexamined":"\nYou pull the handle and the door swings open surprisingly easy. You notice steps that spiral down and disappear into the dark...\n"}

        if "examined" in rooms[2]["examine"]["tapestry"]:
            rooms[2]["west"] = 4

    def roomcommands(self):
        global location
        while True:
            self.check_path()
            command = input(">>> ").lower().split()

            if len(command) == 0:
                self.resetscreen()

            elif command[0] == "help":
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
                print("# List of Commands                                              #")
                print("#                                                               #")
                print("# Moving between rooms:                                         #")
                print("#    Typing 'go north' will make you go through the door        #")
                print("#    located north of you. This also works with the other basic #")
                print("#    cardinal directions (south, east, west) as well as up or   #")
                print("#    down.                                                      #")
                print("#                                                               #")
                print("# Examining items:                                              #")
                print("#    Typing 'examine' followed by an object in the room will    #")
                print("#    give you more information about it.                        #")
                print("#    (i.e. 'examine painting' will tell you about the painting) #")
                print("#                                                               #")
                print("# Taking items:                                                 #")
                print("#    Typing 'get' followed by an item will add it to your       #")
                print("#    inventory.                                                 #")
                print("#    (i.e. 'get stick' will give you a stick)                   #")
                print("#                                                               #")
                print("# When you're ready, press the enter key to continue.           #")
                print("#                                                               #")
                print("#################################################################")
                done = input(">>> ").lower()
                print(done)
                self.resetscreen()

            elif len(command) == 2:
                if command[0] == "get":
                    if command[1] in rooms[location]["items"]:
                        if rooms[location]["items"][command[1]] == "ntaken":
                            self.resetscreen()
                            print("\n" + command[1].upper() + " has been added to your inventory!\n")
                            rooms[location]["items"][command[1]] = "taken"
                        else:
                            self.resetscreen()
                            print("\nYou already took that.\n")
                    else:
                        self.resetscreen()
                        print("\nThat isn't something you can take at the moment.\n")

                elif command[0] == "examine":
                    if command[1] in rooms[location]["examine"]:
                        if "nexamined" in rooms[location]["examine"][command[1]]:
                            self.resetscreen()
                            print(rooms[location]["examine"][command[1]]["nexamined"])
                            rooms[location]["examine"][command[1]] = "examined"
                        else:
                            self.resetscreen()
                            print(rooms[location]["examine2"][command[1]])
                    else:
                        self.resetscreen()
                        print("\nThat's not something you can inspect. Try something else.\n")

                elif command[0] == "go":
                    if command[1] in rooms[location]:
                        location = rooms[location][command[1]]
                        self.resetscreen()
                    else:
                        self.resetscreen()
                        print("\nSorry m8. That's not somewhere you can go at the moment.\n")

                else:
                    self.resetscreen()
                    print("\nNo. Type something else. Preferably use a valid command. Use the 'help' command if you need it.\n")

            else:
                self.resetscreen()
                print("\nNo. Type something else. Preferably use a valid command. Use the 'help' command if you need it.\n")



    def new_game(self):
        global archer,mage,thief,brute, location #is there a way to not use global?
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
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print(rooms[location]["name"].upper())
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        print(rooms[location]["description"])
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
        self.roomcommands()

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
        print("# List of Commands                                              #")
        print("#                                                               #")
        print("# Moving between rooms:                                         #")
        print("#    Typing 'go north' will make you go through the door        #")
        print("#    located north of you. This also works with the other basic #")
        print("#    cardinal directions (south, east, west) as well as up or   #")
        print("#    down.                                                      #")
        print("#                                                               #")
        print("# Examining items:                                              #")
        print("#    Typing 'examine' followed by an object in the room will    #")
        print("#    give you more information about it.                        #")
        print("#    (i.e. 'examine painting' will tell you about the painting) #")
        print("#                                                               #")
        print("# Taking items:                                                 #")
        print("#    Typing 'get' followed by an item will add it to your       #")
        print("#    inventory.                                                 #")
        print("#    (i.e. 'get stick' will give you a stick)                   #")
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

        global rndm_class, player
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




new_game = Story()