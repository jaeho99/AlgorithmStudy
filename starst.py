def solution(moli):
    s = set()
    m = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in moli:
        nx, ny = x + m[i][0], y + m[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x, y, nx, ny))
            s.add((nx, ny, x, y))
            x, y = nx, ny
    return len(s) // 2

# a = 'ULL'
# solution(a)

def solution2(numbers, target):
    answer = [0]
    for i in numbers:
        sub = []
        for j in answer:
            sub.append(j+i)
            sub.append(j-i)
            print(j+1)
        answer = sub
    return answer.count(target)

print(solution2([1,1,1,1,1], 3))