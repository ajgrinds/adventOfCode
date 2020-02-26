with open('input.txt', 'r') as f:
    wires = f.read().splitlines()


def end_points(wire_code):
    wire_points = [(0, 0)]
    for i, pos in enumerate(wire_code):
        if pos[0] == "R":
            wire_points.append((wire_points[i][0], wire_points[i][1] + int(pos[1:])))
        elif pos[0] == "L":
            wire_points.append((wire_points[i][0], wire_points[i][1] - int(pos[1:])))
        elif pos[0] == "U":
            wire_points.append((wire_points[i][0] + int(pos[1:]), wire_points[i][1]))
        elif pos[0] == "D":
            wire_points.append((wire_points[i][0] - int(pos[1:]), wire_points[i][1]))
    return wire_points


def draw(wire):
    points = [(0, 0)]
    for point in wire[1:]:
        if points[-1][0] == point[0]:
            if points[-1][1] > point[1]:
                points.extend((point[0], x) for x in range(points[-1][1] - 1, point[1] - 1, -1))
            else:
                points.extend((point[0], x) for x in range(points[-1][1] + 1, point[1] + 1))
        else:
            if points[-1][0] > point[0]:
                points.extend((x, point[1]) for x in range(points[-1][0] - 1, point[0] - 1, -1))
            else:
                points.extend((x, point[1]) for x in range(points[-1][0] + 1, point[0] + 1))
    return points


wire1_cords = draw(end_points(wires[0].split(",")))
wire2_cords = draw(end_points(wires[1].split(",")))
crosses = set(wire1_cords) & set(wire2_cords)
crosses.remove((0, 0))

# part 1
print(min([abs(point[0]) + abs(point[1]) for point in crosses]))

# part 2
print(min([wire1_cords.index(point) + wire2_cords.index(point) for point in crosses]))
