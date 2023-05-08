from aj_custom_library_cuz_Im_cool import *
import timeit
import time

runs = 1000
start = time.time()


def calc():
    file = list(open("input.txt").read().split("\n"))
    total = 0
    for x in file:
        a, b = x.split(" | ")
        current = [0, 0, 0, 0]
        a = sorted(a.split(" "), key=len)
        for i, y in enumerate(b.split(" ")):
            if len(y) == 2:
                current[i] = 1
            if len(y) == 3:
                current[i] = 7
            if len(y) == 4:
                current[i] = 4
            if len(y) == 7:
                current[i] = 8
            if len(y) == 5:
                if not set(a[0]) - set(y):
                    current[i] = 3
                elif len(set(y) - set(a[2])) == 2:
                    current[i] = 5
                else:
                    current[i] = 2
            if len(y) == 6:
                if set(a[0]) - set(y):
                    current[i] = 6
                elif set(a[2]) - set(y):
                    current[i] = 0
                else:
                    current[i] = 9
        total += int("".join(map(str, current)))
    return total


for _ in range(runs):
    calc()

tt = (time.time() - start) / runs
xx = timeit.Timer(calc).timeit(1)
print(f"average time over {runs} runs:")
print(f"time.time()  benchmark: {tt}")
print(f"timeit.Timer benchmark: {xx}")
print(f"Delta: {abs(tt - xx)} seconds, {abs(tt - xx) / min(tt, xx)}%")


