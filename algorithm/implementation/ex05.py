#뱀

N = int(input())
K = int(input())

board = [[0] * (N+1) for _ in range (N + 1)]
#방향 정보
info = []

#사과 있는곳 1로 표시
for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1

L = int(input())

for _ in range(L):
    X, C = input().split()
    info.append((int(X), C))

#동쪽으로 시작 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, C):
    if C == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    board[x][y] = 2 #뱀 존재하는 위치 2로 표시
    direction = 0 #처음엔 동쪽
    time = 0
    index = 0 #다음에 회전할 정보
    q = [(x, y)] #뱀이 차지하고 있는 위치 정보
    
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        #맵 안에 있고, 몸통 없으면
        if 1 <= x and nx <= N and 1 <= ny and ny <= N and board[nx][ny] != 2:
            #사과 없으면 이동 후 꼬리 제거
            if board[nx][ny] ==0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            #사과 있으면 이동후 꼬리 유지
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))

        #벽이나 뱀의 몸통과 부딪힘
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())