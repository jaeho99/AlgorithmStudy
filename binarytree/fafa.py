# 가운데 노드 찾기
import collections


def findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]]):
    if n <= 1:
        return [0]

    # 양방향 그래프 구성
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    # 첫번째 리프 노드 추가
    leaves = []

    for i in range(n):
        print(f"{graph[i]}나는 i 임 {i}")
        if len(graph[i]) == 1:
            print("다들어오니")
            leaves.append(i)  # 리프 노드 할당

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)  # 그래프에 제거 작업 반영

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)  # 리프 노드 할당

        leaves = new_leaves

    return leaves


print(findMinHeightTrees(4, [[1, 0], [0, 2], [0, 3], [3, 4]]))
