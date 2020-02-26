with open('input.txt', 'r') as f:
    orbits = f.read().splitlines()

indirect_orbits = {}
direct_orbits = {}

for i in orbits:
    direct_orbits[i.split(")")[1]] = i.split(")")[0]
    if i.split(")")[0] in indirect_orbits:
        indirect_orbits[i.split(")")[0]].append(i.split(")")[1])
    else:
        indirect_orbits[i.split(")")[0]] = [i.split(")")[1]]


def indirect(planet):
    total_indirects = 0
    for x in indirect_orbits[planet]:
        if x in indirect_orbits:
            total_indirects += 1 + indirect(x)
        else:
            total_indirects += 1
    return total_indirects


total = 0
for j in indirect_orbits:
    total += indirect(j)

# part 1
print(total)

you = []
current_planet = 'YOU'
while current_planet != "COM":
    current_planet = direct_orbits[current_planet]
    you.append(current_planet)

san = []
current_planet = 'SAN'
while current_planet != "COM":
    current_planet = direct_orbits[current_planet]
    san.append(current_planet)


for j in you:
    if j in san:
        # part 2
        print(you.index(j) + san.index(j))
        break

