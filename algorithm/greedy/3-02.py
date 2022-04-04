#큰수의 법칙

N, M, K = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

#가장 큰 두수
first = data[N - 1]
second = data[N - 2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    result += second
    M -= 1

print(result)

#더 빠른 동작시간

#가장 큰 수가 더해지는 횟수
#count = int(M / (K + 1)) * K
#count += M % (K + 1)

#result = 0
#가장 큰 수 더하기
#result += (count) * first
#두 번째로 큰 수 더하기
#result += (M - count) * second

#print(result)