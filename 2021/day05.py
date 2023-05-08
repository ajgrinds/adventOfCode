from aj_custom_library_cuz_Im_cool import *
from itertools import chain
f = load_str()

grid = [[0 for _ in range(1000)] for _ in range(1000)]
test = 0
for v in f:
    start, end = v.split(" -> ")
    start_x, start_y = map(int, start.split(","))
    end_x, end_y = map(int, end.split(","))
    if start_x == end_x:
        start_y, end_y = (start_y, end_y) if start_y < end_y else (end_y, start_y)
        for y in range(start_y, end_y + 1):
            grid[y][start_x] += 1
    elif start_y == end_y:
        start_x, end_x = (start_x, end_x) if start_x < end_x else (end_x, start_x)
        for x in range(start_x, end_x + 1):
            grid[start_y][x] += 1
    else:
        for y, x in zip(range(start_y, end_y + (1 if start_y < end_y else -1), 1 if start_y < end_y else -1), range(start_x, end_x + (1 if start_x < end_x else -1), 1 if start_x < end_x else -1)):
            grid[y][x] += 1

print(len(list(filter(lambda a: a >= 2, chain(*grid)))))
