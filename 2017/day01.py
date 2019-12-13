with open("input.txt") as f:
    sums = list(map(lambda x: int(x), f.read()))

last = sums[-1]
halfway = len(sums) // 2


def check(x):
    global last
    if x == last:
        last = x
        return True
    else:
        last = x
        return False


def other_check(x):
    global halfway
    if x == sums[halfway]:
        halfway += 1
        if halfway == len(sums):
            halfway = 0
        return True
    else:
        halfway += 1
        if halfway == len(sums):
            halfway = 0
        return False


print(sum(filter(check, sums)))
print(sum(filter(other_check, sums)))
