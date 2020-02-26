import copy
import math
from functools import reduce


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // math.gcd(a, b)


def lcmm(*args):
    """Return lcm of args."""
    return reduce(lcm, args)

formula = open("input.txt").read().splitlines()

dictFormula = {}
for x in formula:
    x = x.split(" => ")
    dictFormula[x[1].split(" ")[1]] = {'makes': int(x[1].split(" ")[0]),
                                       'takes': [z.split(" ") for z in x[0].split(", ")]}


current = {"FUEL": 1}


def takes(material):
    while current[material] > 0:
        for z in dictFormula[material]['takes']:
            if z[1] not in current:
                current[z[1]] = int(z[0])
            else:
                current[z[1]] += int(z[0])
        current[material] -= dictFormula[material]['makes']


while not all(current[item] <= 0 for item in current if item != "ORE"):
    for x in copy.copy(current):
        if x != "ORE":
            takes(x)
print(current["ORE"])

extras = {}
for x in current:
    if x == "ORE" or current[x] == 0:
        continue
    extras[x] = -current[x]



