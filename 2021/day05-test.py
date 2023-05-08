file = open("input.txt")
file_list = file.read().split("\n")

width = 1000
height = 1000
grid = []
for _ in range(height):
    row = []
    for _ in range(width):
        row.append(0)
    grid.append(row)


for line in file_list:
    start, end = line.split(" -> ")
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))
    if x1 == x2:
        y1, y2 = (y1, y2) if y1 < y2 else (y2, y1)
        for y in range(y1, y2 + 1):
            grid[y][x1] += 1
    elif y1 == y2:
        x1, x2 = (x1, x2) if x1 < x2 else (x2, x1)
        for x in range(x1, x2 + 1):
            grid[y1][x] += 1

count = 0
for row in grid:
    for num in row:
        if num > 1:
            count += 1

print(count)

