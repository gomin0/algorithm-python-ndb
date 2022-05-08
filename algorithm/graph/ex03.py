#어두운 길

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

edges = []
result = 0

for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    x, y, z = map(int, input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((z, x, y))

#간선을 비용순으로 정렬
edges.sort()
total = 0 #전체  가로등 비용

for edge in edges:
    cost, a, b = edge
    total += cost
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total - result)