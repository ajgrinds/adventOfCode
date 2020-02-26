import math

with open('input.txt', 'r') as f:
    asteroids = f.read().splitlines()

asteroids = map(lambda asteroid: list(asteroid), asteroids)

positions = []
for y, column in enumerate(asteroids):
    for x, symbol in enumerate(column):
        if symbol == "#":
            positions.append((x, y))


def count(cords, point):
    slopes = map(lambda cord: round(math.atan2(cord[1] - point[1], cord[0] - point[0]), 4), cords)
    return slopes


def points(cords, point):
    slopes = map(lambda cord: (cord, round(math.atan2(cord[1] - point[1], cord[0] - point[0]), 4)), cords)
    return slopes


nums = []
totals = {}
for position in positions:
    nums.append(len(set(count(positions, position))))
    totals[nums[-1]] = position

print(max(nums))


def distance(point, center):
    return math.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)


best_point = totals[max(nums)]

positions.remove(best_point)
destroyed_points = sorted(points(positions, best_point), key=lambda a: a[1])
angles = sorted(list(set(count(positions, best_point))))
current_angle = -1.5708
count = 0
counts = []
while count != 200:
    destroyed = []
    distances = []
    for x in destroyed_points:
        if x[1] == current_angle:
            destroyed.append(x[0])
            distances.append(distance(x[0], best_point))

    if angles.index(current_angle) + 1 == len(angles):
        current_angle = angles[0]
    else:
        current_angle = angles[angles.index(current_angle) + 1]

    for x in destroyed_points:
        if x[0] == destroyed[distances.index(min(distances))]:
            counts.append(x[0])
            destroyed_points.remove(x)
            break
    count += 1

print(counts[199][0] * 100 + counts[199][1])

