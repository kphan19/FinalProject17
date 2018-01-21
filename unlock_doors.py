#Testing/writing code here to only allow moving in a direction if all necessary actions have been executed.
def check_path():
    if "examined" in rooms[1]["examine"]["rug"] and "trapdoor" in rooms[1]["examine"] and "examined" in rooms[1]["examine"]["trapdoor"]:
        rooms[1]["down"] = 2

    elif "examined" in rooms[1]["examine"]["rug"]:
        rooms[1]["examine"]["trapdoor"] = {"nexamined":"\nYou pull the handle and the door swings open surprisingly easy. You notice steps that spiral down and disappear into the dark...\n"}

    if "examined" in rooms[2]["examine"]["tapestry"]:
        rooms[2]["west"] = 4

