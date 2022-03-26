#문자열 뒤집기

S = input()

#0으로 or 1로 뒤집는 횟수
count0 = 0
count1 = 0

if S[0] == '1':
    count0 += 1
else:
    count1 += 0

for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        if S[i] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))  