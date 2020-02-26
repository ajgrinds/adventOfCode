# oooo spooky
from IntCodeComputer import *

points = {}
mapping = [" ",  "█", "▓", "▄", "O"]
score = 0
output = []


def print_output(out, current_score):
    printing = ""
    for i in range(0, len(out) - 2, 3):
        points[(out[i], out[i + 1])] = out[i + 2]
    sorted_points = sorted(points, key=lambda _: _[1])
    printing += f"Score: {current_score}\n"
    for j in range(sorted_points[0][1], sorted_points[-1][1]):
        for i in range(sorted_points[0][0], sorted_points[-1][0]):
            printing += mapping[points[i,j]]
        printing += f"{mapping[1]} \n"
    printing += "\n" * 9
    print(printing, end="")


arcade = IntCodeMachine()
arcade.current_state.stack[0] = 2
done = False
while not done:
    done, output = arcade.calc()
    print_output(output, score)
    ball = paddle = joystick = 0
    for x in range(2, len(output), 3):
        if output[x] == 4:
            ball = output[x - 2]
        if output[x] == 3:
            paddle = output[x - 2]
        if output[x - 2] == -1:
            score = output[x]
    if ball > paddle:
        joystick = 1
    if ball == paddle:
        joystick = 0
    if ball < paddle:
        joystick = -1
    arcade.send_input(joystick)

print(f"Final Score: {score}")

