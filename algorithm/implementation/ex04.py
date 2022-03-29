#https://programmers.co.kr/learn/courses/30/lessons/60059?language=python3

#자물쇠와 열쇠

#90도 회전
def rotate_90(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

#자물쇠 중간 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return  False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    #자물쇠 크기 3배 늘림
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    #새자물쇠 중앙에 기존 자물쇠
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
            
    #열쇠 돌려가며 확인
    for roation in range(4):
        key = rotate_90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                        
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False