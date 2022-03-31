#치킨 배달

from itertools import combinations

N, M = map(int, input().split())
chicken, house = [], []

for r in range (N):
    city = list(map(int, input().split()))
    for c in range(N):
        if city[c] == 1:
            house.append((r, c)) #집
        elif city[c] == 2:
            chicken.append((r, c)) #치킨집

#치킨집 중에서 M개의 치킨집을 뽑기
chooses = list(combinations(chicken, M))

#치킨 거리 합 함수
def get_sum(choose):
    result = 0

    for hx, hy in house:
        #모든 집에 대해 가장 가까운 치킨집
        temp = 1e9
        for cx, cy in choose:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for choose in chooses:
    result = min(result, get_sum(choose))

print(result)