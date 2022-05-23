import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)  # 재귀의 최대 깊이는 기본설정이 1000회 이기에 따로 설정해주는 게 좋다.

N = int(input())

# 트리
tree = [[] for _ in range(N + 1)]
# 부모 노드 저장
parents = [0 for _ in range(N + 1)]
# 트리 구조 입력
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)

def dfs(start, tree, parents):
    for i in tree[start]:
        print("sss")
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)


dfs(1, tree, parents)

for i in range(2, N + 1):   # 0, 1은 상위가 없으니 2부터 시작된다.
    print(parents[i])
