#연산자 끼워 넣기

N = int(input())

#A1~An
A = list(map(int, input().split()))

#덧셈, 뺄셈, 곱셈, 나눗셈 개수
add, sub, mul, div = map(int, input().split())

#최대, 최소 초기화
min_value = 1e9
max_value = -1e9

#DFS 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    #연산자 모두사용하면 최대최소 업데이트
    if i == N:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + A[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - A[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * A[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / A[i]))
            div += 1

dfs(1, A[0])

print(max_value)
print(min_value)