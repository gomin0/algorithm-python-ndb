#https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3

#기둥과 보 설치

def possible(answer):
    for x, y, a in answer:
        if a == 0: #설치된 것이 기둥
            #바닥 위 or 보의 한쪽 끝 or 다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        
        elif a == 1: #설치된 것이 보
            #한쪽 끝이 기둥위 or 양쪽 끝이 다른 보와 동시 연결
            if [x, y -1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 0: #삭제
            answer.remove([x, y, a]) #삭제 실시
            if not possible(answer):
                answer.append([x, y, a]) #가능하지 않은 구조물이면 다시 설치
        if b == 1: #설치
            answer.append([x, y, a]) #설치 실시
            if not possible(answer):
                answer.remove([x, y, a]) #가능하지 않은 구조물이면 다시 삭제
    return sorted(answer)