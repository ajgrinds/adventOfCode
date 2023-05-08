from aj_custom_library_cuz_Im_cool import *

with open("input.txt") as f:
    file, folds = f.read().split("\n\n")
    folds = [x.split(" ")[-1].split("=") for x in folds.splitlines()]
    file = [list(map(int, x.split(","))) for x in file.splitlines()]

grid = [[0 for _ in range(40)] for _ in range(6)]

max_y = 0
def calc_folds(folds, x, y):
    for fold in folds:
        if fold[0] == "x":
            x = int(fold[1]) - abs(int(fold[1]) - x)
        else:
            y = int(fold[1]) - abs(int(fold[1]) - y)
    return x, y


for x, y in file:
    a, b = calc_folds(folds, x, y)
    if y > max_y:
        max_y = y
    grid[b][a] = 1


def process_letter(letter):
    processed = ""
    if letter[0].count(1) == 1:
        if letter[5].count(1) == 4:
            processed = 'L'
        else:
            processed = 'A'
    elif letter[0].count(1) == 2:
        if letter[5].count(1) == 1:
            processed = 'Y'
        elif letter[5].count(1) == 2:
            if letter[2].count(1) == 1:
                if letter[2][3] == 1:
                    processed = 'J'
                else:
                    processed = 'C'
            elif letter[3].count(1) == 2:
                if letter[3][3] == 1:
                    processed = 'U'
                else:
                    processed = 'K'
            else:
                processed = 'H'
        elif letter[5].count(1) == 3:
            processed = 'G'
    elif letter[0].count(1) == 3:
        if letter[5].count(1) == 1:
            processed = 'P'
        elif letter[5].count(1) == 2:
            processed = 'R'
        elif letter[5].count(1) == 3:
            processed = 'B'
    elif letter[0].count(1) == 4:
        if letter[5].count(1) == 4:
            if letter[2].count(1) == 3:
                processed = 'E'
            else:
                processed = 'Z'
        elif letter[5].count(1) == 1:
            processed = 'F'
    return processed

answer = [[], [], [], [], [], [], [], []]
for i in range(0, 6):
    for j in range(8):
        answer[j].append(grid[i][j * 5: j * 5 + 5])

print("".join([process_letter(x) for x in answer]))


count = 0
for row in grid:
    count += row.count(1)
    print(*row)
print(count)
print(max_y)



