import sys

import time
sys.setrecursionlimit(10**9)
n, target = list(map(int, sys.stdin.readline().rstrip().split(' ')))
ran_list = []
for _ in range(n):
    ran_list.append(int(sys.stdin.readline().rstrip()))
def search(ran_list, target, high, low):
    #[802, 743, 457, 539]
    mid = (high + low) // 2

    sum = 0
    for ran in ran_list:
        sum += ran // mid

    if sum > target:
        print(1)
        low = mid+1
        return search(ran_list, target, high, low)

    elif sum < target:
        print(1)
        high = mid-1
        return search(ran_list, target, high, low)

    elif sum == target and high > low:
        print(1)
        low = mid+1
        return search(ran_list, target, high, low)

    elif sum == target:
        print(1)
        return mid

low = 1
high = max(ran_list)//2
print(search(ran_list, target, high , low))
