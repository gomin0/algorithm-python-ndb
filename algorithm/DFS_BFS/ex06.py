#감시 피하기

from itertools import combinations

N = int(input()) #복도 크기
board = [] #복도 정보
teacher = [] #선생님 위치 정보
space = [] #빈 공간 위치 정보

for i in range(N):
    board.append(list(input().split()))
    #선생님 위치 저장
    for j in range(N):
        if board[i][j] == 'T':
            teacher.append((i, j))

        #빈공간 위치 저장
        if board[i][j] == 'X':
            space.append((i, j))
          

#특정 방향으로 감시(발견시 True)
def watch(x, y, direction):
    #왼쪽
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    #오른쪽
    if direction == 1:
        while y < N:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    #위쪽
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    #아래쪽
    if direction == 3:
        while x < N:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

#장애물 설치 후 한 명이라도 걸리는지
def process():
    #모든 선생님 위치 확인
    for x,y in teacher:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False

#빈 공간주 3개 뽑아서 벽 설치
for data in combinations(space, 3):
    for x, y in data:
        board[x][y] = 'O'
    if not process(): #학생 감지 안된 경우
        find = True
        break
    #복구  
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print("NO")