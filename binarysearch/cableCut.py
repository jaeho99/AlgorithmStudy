import sys
from typing import List


def cablecut(array: List, n: int):
    min = 0
    cableMax = max(array)
    while min < cableMax:
        count = 0
        mid = (min + cableMax) // 2

        for x in array:
            count += x // mid

        if count < n:
            cableMax = mid
        else:
            min = mid + 1
    return min - 1 # cnt


K, N = map(int, sys.stdin.readline().split())
ar = []
for _ in range(K):
    ar.append(int((input())))
print(cablecut(ar, N))
# array = [500, 400, 200]