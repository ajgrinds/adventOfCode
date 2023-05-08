file = list(map(int, open("input.txt").read().splitlines()))

total = 0
for i, x in enumerate(file):
    if x > file[i - 1]:
        total += 1

print(total)

