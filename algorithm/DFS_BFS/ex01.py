#특정 거리의 도시 찾기

from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    graph(A).append(B)

#모든 도시 최단거리 초기화
distance = [-1] * [N + 1]
distance[X] = 0 #출발 도시까지 거리 0

#BFS수행
queue = deque([X])
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        #아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            #최단거리 갱신
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

#최단 거리가 K인 모든 도시의 번호를 오름차순으로
check = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        check = True

#만약 최단 거리가 K인 도시가 없다면, -1출력
if check == False:
    print(-1)