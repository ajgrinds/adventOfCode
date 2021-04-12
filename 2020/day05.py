# Advent Of Code 2020 Day 5 Answer
# Code by: Andrew Grindstaff
# https://adventofcode.com/2020/day/5


def main():
    file = open("input.txt").read().splitlines()

    a = set()
    part_2 = 0

    # Part 1: Converts the string of F, B, L and R to a binary number, then gets the decimal version - saves
    # it in a list and stores the highest one
    for x in file:
        string = x.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        num = int(string, 2)
        a.add(num)

    part_1 = len(a)

    # Part 2: A simple for loop to go through the list and find which value is not in it
    for y in a:
        if y - 1 not in a and y - 2 in a:
            part_2 = y - 1

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


def one_line():
    print("Part 1: (one line)")
    print(max(int(x.translate({70:48,66:49,76:48,82:49}),2) for x in open("input.txt").readlines()))

    print("Part 2: (one line)")
    print((max(y:=[int(x.translate({70:48,66:49,76:48,82:49}),2) for x in open("input.txt").readlines()])**2+max(y)-min(y)**2+min(y))/2-sum(y))


if __name__ == '__main__':
    main()
