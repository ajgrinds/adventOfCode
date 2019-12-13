with open("input.txt") as f:
    floors = f.read()

print(floors.count("(") - floors.count(")"))
floor = 0
i = 0
maps = {"(": 1, ")": -1}
while floor >= 0:
    floor += maps[floors[i]]
    i += 1

print(i)
