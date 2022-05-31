import sys

K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]


cable_min = 0
cable_max = max(lan) +1              # array = [400, 500, 200],  n  =  5
    
while cable_min < cable_max:
    count = 0
    mid = (cable_min + cable_max) // 2

    for x in lan:
        count += x // mid
    print(1)
    if count < N:  #
        cable_max = mid  # min                mid            max
    else:
        cable_min = mid + 1

print(cable_min - 1)

# import sys
# from typing import List
#
#
# def cablecut(array: List, n: int):
#     cable_min = 0
#     cable_max = max(array)  # array = [400, 500, 200],  n  =  5
#
#     while cable_min < cable_max:
#         count = 0
#         mid = (cable_min + cable_max) // 2
#
#         for x in array:
#             count += x // mid
#
#         if count < n:  #
#             cable_max = mid  # min                mid            max
#         else:
#             cable_min = mid + 1
#
#     return cable_min - 1  # 길이
#
#
# K, N = map(int, sys.stdin.readline().split())
# ar = []
# for _ in range(K):
#     ar.append(int(sys.stdin.readline()))
# print(cablecut(ar, N))

# array = [500, 400, 200]

#
# ar = []
# for _ in range(K):
#     ar.append(int(sys.stdin.readline()))
# print(cablecut(ar, N))

# array = [500, 400, 200]