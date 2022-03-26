#숫자 카드 게임

N, M = map(int, input().split())

result = 0

#2중 반복문
#for i in range(N):
#    data = list(map(int, input(). split()))
#    min_value = 10001
#    for j in data:
#        min_value = min(min_value, j)
#    result = max(result, min_value)

#min() 함수 사용
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)