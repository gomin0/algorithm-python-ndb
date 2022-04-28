#숨바꼭질

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
#시작 노드를 1번 헛간으로 설정
start = 1
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

#모든 간선 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    #a번 노드와 b번 노드의 이도 비용이 1(양방향)
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i [0]))

dijkstra(start)

max_nod = 0
max_distance = 0
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))