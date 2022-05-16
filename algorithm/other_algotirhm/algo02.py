#소수 판변 함수(제곱근)

import math

#소수 판별 함수
def is_prime_number(x):
    #2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        #x가 해당 수로 나눠떨어지면
        if x % i == 0:
            return False #소수가 아님
    return True #소수임

print(is_prime_number(4))
print(is_prime_number(7))