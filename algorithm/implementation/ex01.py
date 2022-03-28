#럭키 스트레이트

N = input()
length = len(N)
sum_left = 0
sum_right = 0

for i in range(length // 2):
    sum_left += int(N[i])
for i in range(length // 2, length):
    sum_right += int(N[i])
if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")