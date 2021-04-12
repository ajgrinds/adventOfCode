file = open("input.txt").read().splitlines()

x_slopes = [1, 3, 5, 7, 1]
y_slopes = [1, 1, 1, 1, 2]

total = 1
trees = 0

for x_slope, y_slope in zip(x_slopes, y_slopes):
    x = 0
    for y in file[::y_slope]:
        if y[x % len(y)] == "#":
            trees += 1
        x += x_slope
    total *= trees
    trees = 0

print(total)
