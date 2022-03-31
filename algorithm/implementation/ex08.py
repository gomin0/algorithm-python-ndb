#https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3

#외벽 점검

from itertools import permutations

def solution(n, weak, dist):
    #길이를 2배 늘려 원형을 일자로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1
    #0~length-1 위치를 각각 시작점으로
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer