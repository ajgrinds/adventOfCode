# Advent Of Code 2020 Day 1 Answer
# Code by: Andrew Grindstaff
# https://adventofcode.com/2020/day/1


def main():
    file = set(map(int, open("input.txt").read().splitlines()))

    part_1 = 0
    part_2 = 0

    # Part 1: There is only one number that can add with each other number to equal 2020, its as simple as
    # seeing if that number exists. Because we are using sets, it can be even faster
    for x in file:
        if 2020 - x in file:
            part_1 = x * (2020 - x)

    # Part 2: There is only one specific third number that can add with 2 other numbers to equal 2020, same as part 1.
    for x in file:
        for y in file:
            if 2020 - x - y in file:
                part_2 = x * y * (2020 - x - y)

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == '__main__':
    main()
