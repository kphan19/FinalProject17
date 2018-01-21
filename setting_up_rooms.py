# bringing in stuff from main file for testing purposes
import os
def cls():
    """clears screen"""
    os.system('cls' if os.name=='nt' else 'clear')
#----------------------------------------------------------------------------------------------------------------------------------------------
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

# Keeps screen neat by clearing previous commands
def resetscreen():
    cls()
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print(rooms[location]["name"].upper())
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print(rooms[location]["description"])
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")

# Sets parameters to unlock other possible commands
def check_path():
    if "examined" in rooms[1]["examine"]["rug"] and "trapdoor" in rooms[1]["examine"] and "examined" in rooms[1]["examine"]["trapdoor"]:
        rooms[1]["down"] = 2

    elif "examined" in rooms[1]["examine"]["rug"]:
        rooms[1]["examine"]["trapdoor"] = {"nexamined":"\nYou pull the handle and the door swings open surprisingly easy. You notice steps that spiral down and disappear into the dark...\n"}

    if "examined" in rooms[2]["examine"]["tapestry"]:
        rooms[2]["west"] = 4


# This breaks up simple commands. It will look for command words such as go, get, or examine
# in the first part of list i.e. "go down" = list = ["go", "down"] list[0] = "go" and then will use the
# second word to further explain where they're going or what they're retrieving.
def roomcommands():
    global location

    while True:
        check_path()
        command = input(">>> ").lower().split()

        if len(command) == 0:
            resetscreen()

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
            resetscreen()

        elif len(command) == 2:
            if command[0] == "get":
                if command[1] in rooms[location]["items"]:
                    if rooms[location]["items"][command[1]] == "ntaken":
                        resetscreen()
                        print("\n" + command[1].upper() + " has been added to your inventory!\n")
                        rooms[location]["items"][command[1]] = "taken"
                    else:
                        resetscreen()
                        print("\nYou already took that.\n")
                else:
                    resetscreen()
                    print("\nThat isn't something you can take at the moment.\n")

            elif command[0] == "examine":
                if command[1] in rooms[location]["examine"]:
                    if "nexamined" in rooms[location]["examine"][command[1]]:
                        resetscreen()
                        print(rooms[location]["examine"][command[1]]["nexamined"])
                        rooms[location]["examine"][command[1]] = "examined"
                    else:
                        resetscreen()
                        print(rooms[location]["examine2"][command[1]])
                else:
                    resetscreen()
                    print("\nThat's not something you can inspect. Try something else.\n")

            elif command[0] == "go":
                if command[1] in rooms[location]:
                    location = rooms[location][command[1]]
                    resetscreen()
                else:
                    resetscreen()
                    print("\nSorry m8. That's not somewhere you can go at the moment.\n")

            else:
                resetscreen()
                print("\nNo. Type something else. Preferably use a valid command. Use the 'help' command if you need it.\n")

        else:
            resetscreen()
            print("\nNo. Type something else. Preferably use a valid command. Use the 'help' command if you need it.\n")


location = 1
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print(rooms[location]["name"].upper())
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print(rooms[location]["description"])
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
roomcommands()

