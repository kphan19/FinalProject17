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
        "items":{"arrow":"ntaken"}}}

# This breaks up simple commands. It will look for command words such as go, get, or examine
# in the first part of list i.e. "go down" = list = ["go", "down"] list[0] = "go" and then will use the
# second word to further explain where they're going or what they're retrieving.
#command = input(">>> ").lower().split()
#location = 1

#if command[0] == "get":
#    if command[1] in rooms[location]["items"]: