from math import gcd
from functools import reduce

with open('input.txt', 'r') as f:
    moons = f.read().splitlines()


def calc_grav(current, velocity, positions):
    for moon in positions:
        if moon > current:
            velocity += 1
        elif moon < current:
            velocity -= 1
    return velocity


def axis(positions):
    velocities = [0 for _ in positions]
    original = ([x for x in positions], [x for x in velocities])
    total = 0
    while True:
        for x, y in enumerate(zip(positions, velocities)):
            velocities[x] = calc_grav(*y, positions)

        for x, y in enumerate(velocities):
            positions[x] += y
        total += 1

        if (positions, velocities) == original:
            break
    return total


def lcm(denominators):
    return reduce(lambda a, b: a*b // gcd(a, b), denominators)


position = []
for x in moons:
    x = x.split("=")
    x = (int(x[1].split(",")[0]), int(x[2].split(",")[0]), int(x[3].split(">")[0]))
    position.append(x)

velocity = [0 for _ in range(4)]
for a in range(3):
    velocities = [0 for _ in position]
    current_axis = [position[j][a] for j in range(4)]
    for i in range(1000):
        for x, y in enumerate(zip(current_axis, velocities)):
            velocities[x] = calc_grav(*y, current_axis)

        for x, y in enumerate(velocities):
            current_axis[x] += y

    for j in range(4):
        position[j] = tuple([position[j][i] if i != a else current_axis[j] for i in range(3)])
        velocity[j] += abs(velocities[j])

total = 0
for i, j in zip(position, velocity):
    total += (abs(i[0]) + abs(i[1]) + abs(i[2])) * j

print(total)

position = []
for x in moons:
    x = x.split("=")
    x = (int(x[1].split(",")[0]), int(x[2].split(",")[0]), int(x[3].split(">")[0]))
    position.append(x)

print(lcm(axis([position[0][i], position[1][i], position[2][i], position[3][i]]) for i in range(3)))
