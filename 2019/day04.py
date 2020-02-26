import math


def valid(num):
    six_digits = double = non_decreasing = True
    if math.log10(num) != 6:
        six_digits = False
    for x in range(5):
        if num // (x * 10) % 10


total = 0
for num in range(136760, 595730):
    match = False
    triple = []
    for i in range(5):
        if num % 10 > num / 10 % 10:
            break
        if num[i] in triple:
            continue
        if num[i] == num[i + 1]:
            # part 2 for part 1 just remove the if and the else
            if i < 4:
                if num[i] != num[i + 2]:
                    match = True
                else:
                    triple.append(num[i])
            else:
                match = True
    else:
        if match:
            total += 1

print(total)
