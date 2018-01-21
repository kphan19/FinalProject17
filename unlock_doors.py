#Testing/writing code here to only allow moving in a direction if all necessary actions have been executed.
def check_path():
    if "examined" in rooms[1]["examine"]["trapdoor"]:
        rooms[1]["down"] = 2

    if "examined" in rooms[2]["examine"]["tapestry"]:
        rooms[2]["west"] = 4