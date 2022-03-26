#볼링공 고르기

N, M = map(int, input().split())
K = list(map(int, input().split()))

array = [0] * 11

#각 무게의 볼링공 개수
for x in K:
    array[x] += 1

count = 0

for i in range(1, M + 1):
    N -= array[i]
    count += array[i] * N

print(count)