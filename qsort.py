import numpy as np
import random
random.seed()

length = 10

np.random.seed()

def sort(a, l, r):
    i, j = l, r
    while i < j:
        while i < j and a[i] <= a[j]:
            i = i + 1

        if i < j:
            a[i], a[j] = a[j], a[i]

        while i < j and a[i] <= a[j]:
            j = j - 1

        if i < j:
            a[i], a[j] = a[j], a[i]

    if i - 1 > l:
        sort(a, l, i - 1)

    if i + 1 < r:
        sort(a, i + 1, r)

def try_to_sort(x):
    sort(x, 0, len(x) - 1)
    for i in range(len(x) - 1):
        if(x[i] > x[i + 1]):
            print(x)


for _ in range(100):
    x = np.random.randint(1, high = 50, size = length)
    try_to_sort(x)

