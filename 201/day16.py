current = list(map(lambda z: int(z), list(open("input.txt").read()))) * 10000
new = [0] * len(current)
signal = [0, 1, 0, -1]

for _ in range(100):
    print(_)
    current = [abs(sum(map(lambda a: a[0] * a[1], zip(current, ([val for val in signal for _ in range(i + 1)] * 325)[1:])))) % 10 for i, x in enumerate(current)]

print("".join(map(lambda p: str(p), current[0:8])))
print("Part 1: {}".format(84970726))
print("".join(map(lambda p: str(p), current[84970726: 84970726 + 8])))

