from collections import deque
from typing import List

grapgh = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3]
}

def bfs_queue(start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in grapgh[node]:
            if adj not in visited:      # adj 에 가보지 않았다면
                q.append(adj)           # adj 에서도 한번 둘러봐라
                visited.append(adj)     # adj 에 방문했다.

    return visited


assert bfs_queue(1) == [1, 2, 3, 4, 5, 6, 7]


def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result

print(subsets([1, 2, 3]))

a = []
print(id(a))
a.append([])
a.append([1]+[3])
print(a)

for b in range(2, 3):
    print(b)
