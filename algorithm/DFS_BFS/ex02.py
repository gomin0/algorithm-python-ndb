#연구소

N, M = map(int, input().split())
data = []
temp = [[0] * M for _ in range(N)] #벽을 설치한 뒤의 맵 리스트

for _ in range(N):
    data.append(list(map(int, input().split())))

#4가지 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

#dfs사용해 바이러스 퍼트리기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx < N and ny >= 0 and ny < M:
            if temp[nx][ny] == 0:
                #바이러스 전염
                temp[nx][ny] = 2
                virus(nx, ny)

#안전 영역 크기 계산
def safe():
    safe = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                safe += 1
    return safe

#DFS 사용하여 울타리 설치하면서 매번 안전 영역 크기 계산
def dfs(count):
    global result
    #울타리 3개 설치된 경우
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = data[i][j]
        #각 바이러스 위치에서 전파
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)
        #안전영역 최댓값 계산
        result = max(result, safe())
        return
    #빈공간에 울타리 설치(완전탐색)
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                #원상복귀
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)