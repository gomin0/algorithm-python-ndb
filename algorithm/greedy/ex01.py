#모험가 길드

N = int(input())
X = list(map(int, input().split()))
X.sort()

#그룹 수
group = 0
#그룹속 사람 수
count = 0

for i in X:
    count += 1
    if count >= i:
      group += 1
      count = 0

print(group)