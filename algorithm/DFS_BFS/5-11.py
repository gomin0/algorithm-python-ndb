#미로 탈출

from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

#이동 방향(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    #큐가 빌때 까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #공간 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            #괴물인 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문 하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N - 1][M - 1]

print(bfs(0, 0))