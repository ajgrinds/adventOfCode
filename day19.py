import IntCodeComputer
import csv

with open('input.csv', 'r') as f:
    reader = csv.reader(f)
    values = list(reader)[0]

sum = 0
machine = IntCodeComputer.IntCodeMachine(values)
for x in range(50):
    for y in range(50):
        machine.send_input([x, y])
        if machine.calc() == "#":
            sum += 1

print(sum)
