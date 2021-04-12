import IntCodeComputer
import csv

with open('input.csv', 'r') as f:
    reader = csv.reader(f)
    values = list(reader)[0]

machine = IntCodeComputer.IntCodeMachine(values)
output = "".join(map(chr, machine.calc()[1])).splitlines()
answer = []
for i, x in enumerate(output):
    for j, y in enumerate(x):
        try:
            if y == "#":
                if x[j - 1] == "#" and x[j + 1] == "#" and output[i + 1][j] == "#":
                    answer.append(i * j)
        except IndexError:
            continue

print(sum(answer))

machine = IntCodeComputer.IntCodeMachine([2, *values[1:]])
machine.calc()
