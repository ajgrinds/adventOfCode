from aj_custom_library_cuz_Im_cool import *

file = list(open("input.txt").read().split("\n"))
import time
start = time.time()

counts = [42, 17, 34, 39, 30, 37, 41, 25, 49, 45]
# a 8 b 6 c 8 d 7 e 4 f 9 g 7

total = 0
for x in file:
    a = x.split(" | ")[0]
    flat = a.replace(" ", "")
    a = sorted(a.split(" "), key=len)
    nums = {}
    nums["a"] = list(set(a[1]) - set(a[0]))[0]
    flat.replace(nums["a"], "")
    for letter in flat:
        if flat.count(letter) == 9:
            index = "f"
        if flat.count(letter) == 8:
            index = "c"
        if flat.count(letter) == 7:
            if letter in a[2]:
                index = "d"
            else:
                index = "g"
        if flat.count(letter) == 6:
            index = "b"
        if flat.count(letter) == 4:
            index = "e"
        nums[index] = letter


print(time.time() - start)


print(total)



