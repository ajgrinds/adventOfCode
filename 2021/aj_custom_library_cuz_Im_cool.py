import datetime
import itertools
import pyperclip

from textwrap import wrap as split_chars  # split a string every n chars
from statistics import median
from math import factorial


def sum_factorial(n):
    """I am dumb sometimes... 2021.7.2"""
    return n * (n + 1) / 2


def unnest(lis):
    """Unnest a list"""
    return list(itertools.chain(*lis))


def combinations(n1, n2, max_len):
    """Get all combinations with a certain length tbh Im not 100% on what this does"""
    comb = [set(itertools.combinations(range(n1 + n2), i)) - set(itertools.combinations(range(n1), i)) -
            set(itertools.combinations(range(n1, n1 + n2), i)) for i in range(2, max_len + 1)]
    final = []
    for x in comb:
        for z in x:
            final.append(z)
    return final


def all_indexes(arr, symbol):
    """Get the index of every appearance of symbol in i"""
    indexes = []
    for i, v in enumerate(arr):
        if v == symbol:
            indexes.append(i)
    return indexes


def days_between(d1, d2):
    if isinstance(d1, str):
        d1 = datetime.datetime.strptime(d1, "%Y-%m-%d").date()
    if isinstance(d2, str):
        d2 = datetime.datetime.strptime(d2, "%Y-%m-%d").date()
    return abs((d2 - d1).days)


def is_prime(limit: int):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return limit in primes


def get_sec_word(string):
    """Get the second word of a string. Useful for problems that contain DIRECTION DISTANCE or something
    :return int if isdigit()
    """
    answer = string.split(" ")[1]
    if answer.isdigit():
        answer = int(answer)
    return answer


def l_str(arr, separator=''):
    """Converts a list to a string. Useful for an array of numbers"""
    return separator.join(map(str, arr))


def l_int(arr, base=2):
    """Converts a list of strings to a number. Default base is 2, can be specified differently.
    If there is a letter in it, it defaults to 16"""
    if not all(type(x) == int or x.isdigit() for x in arr) and base == 2:
        base = 16
    string = "".join(map(str, arr))
    return int(string, base)


chineseZodiac = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]
zodiacSigns = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def load_int():
    return list(map(int, open("input.txt").read().splitlines()))


def load_str():
    return list(open("input.txt").read().splitlines())


def ans(answer):
    pyperclip.copy(answer)
    print(answer)
    return answer
