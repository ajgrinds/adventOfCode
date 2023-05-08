from aj_custom_library_cuz_Im_cool import *

file = list(open("input.txt").read().splitlines())

new_file = [x for x in file]
opposite = {"}": "{", ">": "<", "]": "[", ")": "("}
score = {")": 3, "]": 57, "}": 1197, ">": 25137}
complete = {"(": 1, "[": 2, "{": 3, "<": 4}
scores = []

total = 0
for x in file:
    open_chunks = []
    points = 0
    for y in x:
        if y not in opposite:
            open_chunks.append(y)
        elif open_chunks[-1] == opposite[y]:
            open_chunks.pop(-1)
        else:
            new_file.remove(x)
            total += score[y]
            break
    else:
        for z in open_chunks[::-1]:
            points *= 5
            points += complete[z]
        scores.append(points)

print(total)
print(scores)

print(median(scores))
