def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for co, pri in enumerate(prices):
        while stack and pri < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = co - last
        stack.append(co)

    return answer


# def solution(prices):
#     answer = []
#     for c in prices:
#         count = 0
#         last = c
#
#         for t in range(len(prices) - prices.index(c)-1):
#             # print(t)
#             print(f"ss{c}")
#             print(len(prices) - prices.index(c) - 1)
#             count += 1
#             if last >= t:
#                 answer.append(count)
#                 break
#
#     answer.append(0)
#     return answer
def solution(prices):
    answer = [0] * len(prices)
    for c, p in enumerate(prices):
        if c == len(prices):
            break
        for y in range(c + 1, len(prices)):
            if prices[c] <= prices[y]:
                answer[c] += 1
            else:
                answer[c] += 1
                break
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
# dic = {"김":1}
# dic["김"].append({"재호":2})
# print(dic["김"])
