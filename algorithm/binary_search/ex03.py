#공유기 설치

#집개수(N), 공유기 개수(C)
n, c = list(map(int, input().split()))

array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

start = 1 #가능한 최소 갭(min gap)
end = array[-1] - array[0] #가능한 최대 갭(max gap)
result = 0

while(start <= end):
    mid = (start + end) // 2 #mid는 가장 인접한 두 공유기 사이의 갭
    value = array[0]
    count = 1
    #현재 mid값을 이용해 공유기 설치
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: #C개 이상의 공유기를 설치할 수 있는 경ㅇ우, 갭을 증가
        start = mid + 1
        result = mid
    else:
        end = mid -1

  print(result)