#https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

#실패율

def solution(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i) #i에 
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
            
        answer.append((i, fail))
        length -= count
        

    #실패율 기준 내림차순
    answer = sorted(answer, key=lambda t: t[1], reverse = True)
    
    answer = [i[0] for i in answer]
    
    return answer