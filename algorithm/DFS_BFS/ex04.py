#https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

#괋호 변환

#균형잡힌 괄호 문장열 인덱스
def balance(p):
    count = 0 #왼쪽 괄호 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

#올바른 괄호 문자열인지
def check(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
        return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balance(p)
    u = p[:index + 1]
    v = p[index + 1:]
    #올바른 문자열이면, v앧 대해 함수 수행 결과 붙여 반환
    if check(u):
        answer = u + solution(v)
    #올바르지 않으면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) #첫번째와 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
