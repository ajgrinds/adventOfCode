from aj_custom_library_cuz_Im_cool import *

#file = list(open("input.txt").read().splitlines())
file = list(map(int, open("input.txt").read().split(",")))

nums = [0] * 9
for v in file:
    nums[v] += 1

print(nums)

for x in range(256):
    zero = nums[0]
    for y in range(1, 9):
        nums[y - 1] = nums[y]
    nums[6] += zero
    nums[8] = zero

print(nums)
print(sum(nums))
