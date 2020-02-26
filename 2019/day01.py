with open('input.txt', 'r') as f:
    masses = f.read().splitlines()

fuel = list(map(lambda mass: int(mass) // 3 - 2, masses))
fuel_total = sum(fuel)

# part 1
print(fuel_total)

for num in fuel:
    added_fuel = num // 3 - 2
    while added_fuel > 0:
        fuel_total += added_fuel
        added_fuel = added_fuel // 3 - 2

# part 2
print(fuel_total)
