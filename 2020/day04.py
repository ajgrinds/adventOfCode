file = open("input.txt").read().split("\n\n")


def check(string):
    return all(word in string.replace("\n", " ") for word in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


part_1 = 0
part_2 = 0
filtered_file = filter(check, file)
for x in filtered_file:
    part_1 += 1
    a = {}


    def assign(z, b):
        a[z] = b


    for i in map(lambda y: y.split(":"), x.replace("\n", " ").split()):
        assign(*i)

    if not (len(a["byr"]) == 4 and a["byr"].isdigit() and 1920 <= int(a["byr"]) <= 2002):
        continue
    if not (len(a["iyr"]) == 4 and a["iyr"].isdigit() and 2010 <= int(a["iyr"]) <= 2020):
        continue
    if not (len(a["eyr"]) == 4 and a["eyr"].isdigit() and 2020 <= int(a["eyr"]) <= 2030):
        continue
    if not (len(a["hgt"]) == 4 or len(a["hgt"]) == 5):
        continue
    elif len(a["hgt"]) == 4:
        if a["hgt"][-2:] != "in":
            continue
        if not 59 <= int(a["hgt"][:-2]) <= 76:
            continue
    elif len(a["hgt"]) == 5:
        if a["hgt"][-2:] != "cm":
            continue
        if not 150 <= int(a["hgt"][:-2]) <= 193:
            continue
    if not (a["hcl"][0] == "#" and len(a["hcl"]) == 7):
        continue
    if a["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue
    if not (a["pid"].isdigit() and len(a["pid"]) == 9):
        continue
    part_2 += 1

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
