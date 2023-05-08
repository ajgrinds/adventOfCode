import itertools


def combinations(n1, n2, max_len):
    """Get all combinations with a certain length tbh Im not 100% on what this does"""
    ans = [set(itertools.combinations(range(n1 + n2), i)) - set(itertools.combinations(range(n1), i)) -
           set(itertools.combinations(range(n1, n1 + n2), i)) for i in range(2, max_len + 1)]
    final = []
    for x in ans:
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

