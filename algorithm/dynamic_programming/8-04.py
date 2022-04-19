#피보나치 수열 소스코드(반복적)

#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

#보텀업 다이나믹 프로글래밍
for i in range(3, n+ 1):
   d[i] = d[i - 1] + d[i - 2]

print(d[n])