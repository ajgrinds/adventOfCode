from aj_custom_library_cuz_Im_cool import *
from textwrap import wrap
nums = list(map(int, open("input.txt").read().splitlines()[0].split(",")))

boards = list(map(lambda x: x.splitlines(), open("input.txt").read().split("\n\n")[1:]))
totals = [len(nums)] * len(boards)


for i, board in enumerate(boards):
    highest = len(nums)
    for j in range(5):
        across = max(nums.index(list(map(int, wrap(board[j], 2)))[k]) for k in range(5))
        down = max(nums.index(list(map(int, wrap(board[k], 2)))[j]) for k in range(5))
        highest = min(highest, down, across)
    totals[i] = highest

final = list(map(int, wrap(" ".join(boards[totals.index(min(totals))]), 2)))

print(sum(set(final) - set(nums[:min(totals) + 1])) * nums[min(totals)])

final = list(map(int, wrap(" ".join(boards[totals.index(max(totals))]), 2)))
print(sum(set(final) - set(nums[:max(totals) + 1])) * nums[max(totals)])
