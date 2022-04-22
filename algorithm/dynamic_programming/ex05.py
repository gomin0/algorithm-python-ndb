#못생긴 수

n = int(input())

ugly = [0] * n #못생긴 수를 담기 위한 테이블(1차원 DP 테이블)
ugly[0] = 1 #첫 번째 못생긴 수는 1

#2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
#처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

#1부터 n까지의 못생긴 수를 찾기
for i in range(1, n):
    ugly[i] = min(next2, next3, next5)
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

#n번째 못생긴 수 출력
print(ugly[n - 1])