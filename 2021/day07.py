from aj_custom_library_cuz_Im_cool import *

file = list(map(int, open("input.txt").read().split(",")))

total = 0
med = median(file)
for x in file:
    total += abs(med - x)

print(total)

min_gas = None
for i in range(min(file), max(file)):
    gas = 0
    for x in file:
        n = (abs(x - i))
        gas += (n * (n+1))/2
    if min_gas is None or gas < min_gas:
        min_gas = gas

print(min_gas)
