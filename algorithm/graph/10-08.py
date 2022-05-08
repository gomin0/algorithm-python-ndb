#커리큘럼

from collections import deque
import copy

v = int(input())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]
time = [0] * (v + 1)

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] #첫 번째 수는 시간 정로를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time) #알고리즘 수행 결과를 담을 리스트
    q = deque() #큐 기능을 위한 deque 라이브러리 사용
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])

topology_sort()