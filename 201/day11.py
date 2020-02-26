from adventOfCode2019.IntCodeComputer import *

robot = IntCodeMachine(_input=[0])
current_point = (0, 0)
direction = 0
# ^ = 0
# > = 1
# v = 2
# < = 3
painted = {}


def move(point, rl):
    if rl == 0:
        point = (point[0], point[1] + 1)
    elif rl == 1:
        point = (point[0] + 1, point[1])
    elif rl == 2:
        point = (point[0], point[1] - 1)
    elif rl == 3:
        point = (point[0] - 1, point[1])
    return point


done = False
while not done:
    done, output = robot.calc()
    if not output:
        robot.send_input(painted[current_point] if current_point in painted else 0)
    else:
        painted[current_point] = output[0]
        if output[1] == 1:
            direction += 1
        else:
            direction -= 1
        direction %= 4
        current_point = move(current_point, direction)
        robot.send_input(painted[current_point] if current_point in painted else 0)

print(len(painted))

for y in range(sorted(painted.keys(), key=lambda j: j[1])[-1][1] - sorted(painted.keys(), key=lambda j: j[1])[0][1] + 1):
    for x in range(sorted(painted.keys())[-1][0] - sorted(painted.keys())[0][0]):
        try:
            if painted[(x, -y)] == 1:
                print("@", end="")
            else:
                print(" ", end="")
        except KeyError:
            print(" ", end="")
    print()

