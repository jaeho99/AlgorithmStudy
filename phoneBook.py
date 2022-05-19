import math
# def solution(phone_book):
#     for c, pre in enumerate(phone_book):
#         for u in range(c+1, len(phone_book)):
#             if pre == phone_book[u][:len(pre)]:
#                 return False
#     return True
import collections
def solution(phone_book):
    answer = True
    for c, n in enumerate(phone_book):
        for u in range(c + 1, len(phone_book)):
            if n == phone_book[u][:len(n)]:
                print(f"접두사 발견 n:{n} 얘랑 {phone_book[u]}")
                return False
    return True


# def solution(phone_book):
#     for c, pre in enumerate(phone_book):
#         for u in range(c+1, len(phone_book)):
#             if len(phone_book[u]) >= len(pre) and pre.__eq__(phone_book[u][:len(pre)]):
#                 return False
#     return True

# phone_book = ["12","15523","252124", "123"]
# print(solution(phone_book))
# print("s".__eq__("s"))



# 프로그래머스 문제 기능개발
def sol(progresses, speeds):

    answer = []

    chk = collections.deque()  # deque를 이용하여 왼쪽부터 비교하여 pop으로 제거 하는 형식 시도
    for a in range(len(progresses)):
        chk.append(math.ceil((100-progresses[a])/speeds[a]))    # chk에 작업에 걸리는 일 수를 저장
    tlk = chk[0]                    # 비교할 작업 값 초기값 지정
    count = 1                       # 작업일 최소값 1

    for b in range(1, len(chk)):    # chk[0] 값 비교부터 시작되기 때문에 1부터 시작
        if tlk < chk[b]:            # tlk(제출 작업일) < chk[b](함께 제출할 작업일)
            answer.append(count)    # 함께 제출 가능한 작업 제출
            tlk = chk[b]            # 제출이 진행 됐으므로 함께 제출 작업일이 제출 작업일로 변경
            count = 1               # 함께 가능한 제출 개수 초기화
        else:
            count += 1              # if 통과시 함께 제출 가능 이므로 +1
    answer.append(count)            # 혼자 남은 작업 or 현재까지 함께 제출가능한 작업을 최종 제출
    return answer



progresses = [95, 90, 99, 99, 80, 99, 70]
speeds = [1, 1, 1, 1, 1, 1, 20]
sol(progresses, speeds)
