#https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

#문자열 압축

def solution(s):
    answer = len(s)
   #1부터 전체 길이 절반까지 잘라봄
    for i in range(1, len(s) // 2 + 1):
        compressed = ""
        cut = s[0:i]
        count = 1
        for j in range(i, len(s), i):
            if cut == s[j:j + i]:
                count += 1
            else:
                compressed += str(count) + cut if count >= 2 else cut
                cut = s[j:j + i]
                count = 1
        #나머지
        compressed += str(count) + cut if count >= 2 else cut
        answer = min(answer, len(compressed))
        
    return answer