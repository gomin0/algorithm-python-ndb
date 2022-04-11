#인구 이동

from collections import deque

N, L, R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def bfs(x, y, index):
    #(x, y)의 위치와 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = A[x][y] #현재 연합 인구 수
    count = 1 #현재 연합 국가 수
    #큐가 빌때 까지
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(A[nx][ny] - A[x][y]) <= R:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += A[nx][ny]
                    count += 1
                    united.append((nx, ny))

    for i, j in united:
        A[i][j] = summary // count #인원 분배
    return count

total_count = 0

while True:
    union = [[-1] * N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if union[i][j] == -1: #해당 나라가 아직 처리 않됐으면
                bfs(i, j, index)
                index += 1
    if index == N * N:
        break
    total_count += 1

print(total_count)