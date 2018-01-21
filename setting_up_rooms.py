rooms = {
    1 :{"name":"Start",
        "description":"\nYou wake up on a cold floor. Don't ask me how you got there. You sit up and decide to take a look around and take in your surroundings.\nCovering the floor across from you is a dusty ol' rug. The walls are tall and made of stone. On one of them, there is an unsettling portrait \nof some random old lady. Opposite the painting is a small window. In the corner you spy a chest. Standing up, you check your pockets and find:\n1 gold\n1 silver\n10 copper\nand a crumpled up note...\n\nThe note reads:\n\"WELCOME TO THE ONCE GREAT KINGDOM OF AZURON. SO SORRY ABOUT YOUR CURRENT SITUATION BUT IT COULDN'T BE HELPED.\nYOUR OVERALL GOAL IS TO ESCAPE THIS CASTLE IN ONE PIECE (PREFERABLY ALIVE), HOWEVER THERE ARE MANY OTHER THINGS TO DO WHILE YOU'RE HERE.\nTHIS ROOM WILL SERVE AS YOUR TUTORIAL. I WISH YOU THE BEST OF LUCK.\"\nTry using the 'examine' command (i.e. 'examine painting').\n",
        "down": 2,
        "examine":{"door":"\nOf course you would try the door. Unfortunately, it's locked up and barred nice and tight. No getting through there m8.",
                   "window":"\nYou peek your head out the window and realize that if you jump out, you'd end up being very, very dead.\nThe room you're in seems to be in some high up tower. There aren't any vines within arms reach that you could use to shimmy down the side either.\nWhat a shame.",
                   "wall":"\nYou look closely at the wall, hoping for some kind of clue as to what you're doing. You see nothing but tiny tally marks...alot of them.\n",
                   "rug":"\nThe rug looks expensive. As you go to take a look at it, something rattles...You flip it up and find...SHOCKER a trapdoor.\n",
                   "trapdoor":"\nYou pull the handle and the door swings open surprisingly easy. You notice steps that spiral down and disappear into the dark...\n",
                   "painting":"\nYou look at the old painting. Its eyes are so serious. It seems to be looking at something. You follow its gaze to the corner and see\na stick of some sort in the corner. Try using the \"get\" command. (\"get\" followed by item so \"get stick\")\n",
                   "chest":""},
        "items":{"stick":"ntaken"}},
    2 :{"name":"Dining Hall",
        "description":"\nYou stumble through a heavy pair of doors into what appears to be a Dining Hall. You look around and see a large table in the center of the room,\na large tapestry on the west wall, a chest in the corner, and doors on the northern and eastern walls.\n",
        "north":6,
        "east":3,
        "west":4,
        "examine":{"table":"\nYou walk over to the table and see an arrow stuck on the tablecloth.\n",
                   "tapestry":"\nThere's a slight breeze coming from...behind the fabric? You give the tapestry a tug and the whole thing falls down\ncausing a cloud of dust to explode in your face. When the dust settles, you find another set of doors!\n",
                   "chest":"\nYou go to open the chest hoping to find something useful. Instead, when you lift the lid, a tiny little dart shoots out at you\nand gets you in the arm...how unfortunate. Luckily it didn't do too much damage, but in the future be cautious of possible traps.\n",
                   "door":"\nUse 'go' followed by a direction (north,west,east,south,up,down) to go through a door.\n"},
        "items":{"arrow":"ntaken"}},
    3 :{"name":"Kitchen",
        "description":"\nYou open the door to what seems to be a kitchen. As you step in...oh dear. The floor gives way under you and you fall...\n",
        "examine":"",
        "items":{"spoon":"ntaken"}},
    4 :{"name":"Library",
        "description":"\nYou push on the doors. The light streaming in through the window in front of you is almost blinding. Once you're eyes adjust, \nyou realize you seem to be in some old library with a large, dusty shelf lining the wall.\n",
        "north":6,
        "east":2,
        "west":5,
        "examine":{"window":"\nYou walk over to the west wall, in front of the giant set of windows, and give it a push. Surprisingly, it swings open with ease.\nOutside you see a huge yard. You could probably climb through the window if you tried...\n",
                   "shelf":"\nYou swipe your finger along the shelf and disrupt a very thick layer of dust. Then you notice a book sitting all by itself in the corner.\n",
                   "book":"\nOpening the book, you make the mistake of flipping through the pages revealing...more dust. Good job.\n"},
        "items":{"book":"ntaken"}},
    5 :{"name":"Courtyard",
        "description":"\nHECK YEA BABY! FREE AT...last? Ha no, not that easy. You look around and notice the entire yard is surrounded by very large, concrete walls.\nToo bad, so sad. Off to the side, you see a piece of rope.\n",
        "east":4,
        "examine":{"wall":"\nUnfortunately, the wall is too tall for you to climb, even with a rope. There is no hope of escape. Just give up.\n",
                   "rope":"\nIt's a decent length of rope. Could be useful later on.\n"},
        "items":{"rope":"ntaken"}},
    6 :{"name":"Ballroom",
        "description":"\nOoo. A spooky ballroom. There's barely any light coming into the room, making it extra spooky, and for good reason. DA DA!\nYour first monster has appeared!\n"}}

# This breaks up simple commands. It will look for command words such as go, get, or examine
# in the first part of list i.e. "go down" = list = ["go", "down"] list[0] = "go" and then will use the
# second word to further explain where they're going or what they're retrieving.
#command = input(">>> ").lower().split()
#location = 1

#if command[0] == "get":
#    if command[1] in rooms[location]["items"]: