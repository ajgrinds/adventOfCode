from aj_custom_library_cuz_Im_cool import *

file = list(map(lambda x: list(map(int, x)), open("input.txt").read().split("\n")))
print(file)
lows = []
sizes = []
total = 0
for i, x in enumerate(file):
    for j, y in enumerate(x):
        y = int(y)
        up = down = left = right = False
        try:
            if y < int(x[j + 1]):
                left = True
        except IndexError:
            left = True

        if y < int(x[j - 1]) or j - 1 == -1:
            right = True
        if y < int(file[i - 1][j]) or i - 1 == -1:
            up = True
        try:
            if y < int(file[i + 1][j]):
                down = True
        except IndexError:
            down = True
        if up and down and left and right:
            total += y + 1
            lows.append((i, j))


def find_size(grid, y_coord, x_coord):
    count = 1
    grid[y_coord][x_coord] = 9
    if x_coord + 1 != len(grid) and grid[y_coord][x_coord + 1] != 9:
        count += find_size(grid, y_coord, x_coord + 1)

    if y_coord + 1 != len(grid) and grid[y_coord + 1][x_coord] != 9:
        count += find_size(grid, y_coord + 1, x_coord)

    if y_coord != 0 and grid[y_coord - 1][x_coord] != 9:
        count += find_size(grid, y_coord - 1, x_coord)

    if x_coord != 0 and grid[y_coord][x_coord - 1] != 9:
        count += find_size(grid, y_coord, x_coord - 1)

    return count


for low in lows:
    sizes.append(find_size(file, low[0], low[1]))

ans = sorted(sizes)[-3:]
print(ans[0] * ans[1] * ans[2])

