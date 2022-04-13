#안테나

n = int(input())
houses = list(map(int, input().split()))
houses.sort()

#중간 값 출력
print(houses[(n-1) // 2])