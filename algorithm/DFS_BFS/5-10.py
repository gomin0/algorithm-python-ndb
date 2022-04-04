#음료수 얼려 먹기

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    #범위에서 벗어나면 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    #아직 방문 안했으면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

#모든 노드(위치)에 대해 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        #현재 위치에 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)