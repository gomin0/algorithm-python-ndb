#게임 개발

N, M = map(int, input().split())
#방문한 곳 처리 배열
d = [[0] * M for _ in range(N)]
#현재 위치와 방향
x, y, direction = map(int, input().split())
#현재 위치 방문 처리
d[x][y] = 1

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#왼쪽으로 방향 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[ny][nx] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    #갈 데 없음
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)