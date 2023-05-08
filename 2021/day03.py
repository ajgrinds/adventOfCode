from aj_custom_library_cuz_Im_cool import *
file = load_str()

zero_count = [0,0,0,0,0,0,0,0,0,0,0,0]
one_count = [0,0,0,0,0,0,0,0,0,0,0,0]

for x in file:
    for i in range(12):
        if x[i] == "0":
            zero_count[i] += 1
        else:
            one_count[i] += 1
total = [0,0,0,0,0,0,0,0,0,0,0,0]
anti = [1,1,1,1,1,1,1,1,1,1,1,1]
for i in range(12):
    if one_count[i] > zero_count[i]:
        total[i] = 1
        anti[i] = 0


print(l_int(total) * l_int(anti))

file = load_str()

zero_count = 0
one_count = 0
current_position = 0

while True:
    zero_count = 0
    one_count = 0
    for x in file:
        if x[current_position] == "1":
            one_count += 1
        else:
            zero_count += 1

    new_file = []
    higher = "1" if one_count >= zero_count else "0"
    for x in file:
        if x[current_position] == higher:
            new_file.append(x)

    file = new_file

    if len(file) <= 1:
        answer = file[0]
        break
    current_position += 1

current_position = 0
file = load_str()
while True:
    zero_count = 0
    one_count = 0
    for x in file:
        if x[current_position] == "1":
            one_count += 1
        else:
            zero_count += 1

    new_file = []
    higher = "1" if one_count < zero_count else "0"
    for x in file:
        if x[current_position] == higher:
            new_file.append(x)

    file = new_file

    if len(file) <= 1:
        secanswer = file[0]
        break
    current_position += 1

print(l_int(answer) * l_int(secanswer))