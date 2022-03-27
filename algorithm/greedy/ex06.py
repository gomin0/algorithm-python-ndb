#https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
#무지의 먹방 라이브

import heapq

def solution(food_times, k):
    #더 섭취할 음식이 없으면 -1
    if sum(food_times) < k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        #(음식 시간, 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
        
    sum_value = 0 #먹기 위해 사용한 시간
    previous = 0 #직전에 다 먹은 음식 시간
    length = len(food_times) #남은 음식의 개수
    
    #sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 K 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 #다 먹은 음식 제외
        previous = now #이전 음식 시간 재설정
        
    result = sorted(q, key = lambda x: x[1]) #번호 순 정렬
    return result[(k - sum_value) % length][1]