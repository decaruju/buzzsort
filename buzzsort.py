import random
import itertools
import math


def maximum_number_of_inversions(lst):
    return len(lst)*(len(lst)-1)//2


def ordered_pairs(lst):
    for i in range(len(lst)):
        for j in range(i):
            yield lst[j], lst[i]


def number_of_inversions(lst):
    return sum(int(x > y) for x, y in ordered_pairs(lst))


def buzzsort(lst):
    lst = lst[:]
    shuffles = 0
    while (inversions := number_of_inversions(lst)) != 0:
        shuffles += 1
        switches = random.choices(
            list(itertools.combinations(list(range(len(lst))), 2)),
            k=math.ceil(inversions/3),
        )
        for i, j in switches:
            lst[i], lst[j] = lst[j], lst[i]

    return lst, shuffles

def bogosort(lst):
    lst = lst[:]
    shuffles = 0
    while any(lst[i] > lst[i+1] for i in range(len(lst) - 1)):
        shuffles += 1
        random.shuffle(lst)
    return lst, shuffles


lst = list(range(10))
random.shuffle(lst)
print(buzzsort(lst))
print(bogosort(lst))
