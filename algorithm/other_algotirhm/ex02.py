#암호 만들기

from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u') #5개의 모음 정의
l, c = map(int, input().split())

#가능한 암홀를 사전식으로 출력해야 하므로 입력 이후에 정렬 수행
array = input().split(' ')
array.sort()

#길이가 l인 모든 암호 조합 확인
for password in combinations(array, l):
    #패스워드에 포함된 각 문잘를 확인하며 모음의 개수 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    #최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if count >= 1 and count <= l - 2:
        print(''.join(password))