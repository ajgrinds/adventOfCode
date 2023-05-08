file = list(open("input.txt").read().splitlines())

x = 0
y = 0
depth = 0

for z in file:
    if "forward" in z:
        x += int(z.split(" ")[1])
        depth += y * int(z.split(" ")[1])

    if "up" in z:
        y -= int(z.split(" ")[1])
    if "down" in z:
        y += int(z.split(" ")[1])

print(x * depth)
