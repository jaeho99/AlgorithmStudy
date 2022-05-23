# class Node:
#     def __init__(self):
#         self.child = None
#     1 6   6 3    3 5           트리를 만들기 위한 테스트 시작
# a, b = 1, 6
# c, d = 6, 3
# e, f = 3, 5
# deQueue 에 넣어서 하나씩 뺀다?
# t = {1: {6: {5: 5}, 5: 7}}
# t[1][6] = 8, {5: 5}
# if t.get(1):                  딕셔너리의 키 값이 존재여부 확인이 되는지 체크
#     print("있네")
# else:
#     print("없네")

# t = {1: 3}
# if t.get(1):
#     t[1] = 6
#
# if t[1].get(6):
#     t[1][6] = 3
#
# print(t)

# t = {1: 2}
# t[1] += 2
# print(t)
from collections import deque

a = deque()
a.append({1: 6})
a.append({6: 3})
a.append({3: 5})
a.append({4: 1})
a.append({2: 4})
a.append({4: 7})
b = a.popleft()
c = a.popleft()
print(b)
