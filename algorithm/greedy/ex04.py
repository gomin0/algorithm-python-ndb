#만들 수 없는 금액

N = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1

for x in coin:
    if target < x:
        break
    target += x

print(target)