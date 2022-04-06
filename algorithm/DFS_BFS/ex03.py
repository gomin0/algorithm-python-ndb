#경쟁적 전염

from collections import deque

N, K = map(int, input().split())

graph = [] #전체 보드 정보
data = [] #바이러스 정보

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        #바이러스가 존재하는 경우 data에 삽입(종류, 시간, 위치)
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

#정렬 하고 큐로 옮기기
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

#BFS 진행
while q:
    virus, s, x, y = q.popleft()
    #s초 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    #4가지 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            #아직 방문안했으면 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])