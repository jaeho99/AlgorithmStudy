import heapq

from heap.structures import BinaryMaxHeap


def test_maxheap_we_mad(lst, k):
    maxheap = BinaryMaxHeap()

    for elem in lst:
        maxheap.insert(elem)

    return [maxheap.extract() for _ in range(k)][k - 1]


def test_maxheap_heapq(lst, k):
    return heapq.nlargest(k, lst)[-1]


assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1

n = int(input())
a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
b = [3, 2, 1, 5, 6, 4]

# def solution(lst, n):
#     heapq.heapify(lst)
#     print(lst)
#     for c, e in enumerate(a[::-1]):
#         print(e)
#         if c == n -1  :
#             return e
#     return f"배열은 {len(lst)} 번째까지 존재합니다."
def solution(lst, n):
    heapq.heapify(lst)

    for _ in range(len(lst) - n):
        print(lst)
        print(heapq.heappop(lst))

    return heapq.heappop(lst)



print(solution(b, n))
