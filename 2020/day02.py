# Advent Of Code 2020 Day 2 Answer
# Code by: Andrew Grindstaff
# https://adventofcode.com/2020/day/2

def main():
    file = open("input.txt").read().splitlines()

    part1 = 0
    part2 = 0
    for string in file:
        temp, password = string.split(":")
        numbers, letter = temp.split(" ")
        first, second = map(int, numbers.split("-"))

        # Part 1: Ensure that the count (number) of each letter is between the first and second (our two limits)
        if first <= password.count(letter) <= second:
            part1 += 1

        # Part 2: Check both positions of the password to see if they equal letter. Then check they do not equal each
        # other using != (effectively xor)
        if (password[first] == letter) != (password[second] == letter):
            part2 += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    main()
