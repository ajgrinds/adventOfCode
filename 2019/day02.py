import csv
from itertools import permutations


def calc(value1, value2):
    with open('input.csv', 'r') as f:
        reader = csv.reader(f)
        values = list(reader)[0]

    values = list(map(lambda value: int(value), values))
    values[1] = value1
    values[2] = value2

    i = 0
    while i < len(values):
        if values[i] == 1:
            values[values[i + 3]] = values[values[i + 1]] + values[values[i + 2]]
        elif values[i] == 2:
            values[values[i + 3]] = values[values[i + 1]] * values[values[i + 2]]
        elif values[i] == 99:
            break
        i += 4
    return values


# part1
print(calc(12, 2)[0])

# part2
answer = 19690720
nums = permutations([i for i in range(99)], 2)
result = list(filter(lambda num: calc(num[0], num[1])[0] == answer, nums))[0]
print(result[0] * 100 + result[1])
