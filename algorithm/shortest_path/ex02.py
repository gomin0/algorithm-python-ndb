#정확한 순위

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받가 그 값으로 초기화
for _ in range(m):
    #A 에서 B로 가는 비용 1
    a, b = map(int, input().split())
    graph[a][b] = 1

#점화식 따라 플로이드 워셜
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
        if count == n:
            result += 1
print(result)