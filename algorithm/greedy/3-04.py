#1이 될 때까지
N, K = map(int, input().split())

count = 0
#while N > 1:
#    if N % K == 0:
#        N /= K
#        count += 1
#    else:
#        N -= 1
#        count += 1

while True:
    #1빼기 카운트
    target = (N // K) * K
    count += (N - target)
    N = target
    if N < K:
        break
    count += 1
    N //= K

count += (N - 1)


print(count)