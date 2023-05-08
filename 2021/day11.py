from aj_custom_library_cuz_Im_cool import *

file = open("input.txt").read().splitlines()
new_file = []
for x in file:
    new_file.append(list(map(int, (y for y in x))))

perms = set(itertools.combinations([-1, 0, 1] * 2, 2))
perms.remove((0, 0))

print(perms)


flashed = set()
def calc_flash(l, y, x):
    flashes = 0
    if l[y][x] > 9 and (y, x) not in flashed:
        flashes += 1
        flashed.add((y, x))
        for dy, dx in perms:
            if len(l) > y + dy >= 0 and len(l[y + dy]) > x + dx >= 0:
                l[y + dy][x + dx] += 1
                flashes += calc_flash(l, y + dy, x + dx)
    return flashes


total = 0
for i in range(1000):
    for y in range(len(new_file)):
        for x in range(len(new_file[y])):
            new_file[y][x] += 1
    for y, row in enumerate(new_file):
        for x, num in enumerate(row):
            total += calc_flash(new_file, y, x)
    for y, x in flashed:
        new_file[y][x] = 0
        if len(flashed) == 100:
            print(i + 1)
            exit(1)
    flashed = set()

print(new_file)
print(total)
