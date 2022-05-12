#청소년 상어

import copy

#4 x 4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    #메 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        #각 위치마다 [물고기 번호, 방향]을 저장
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

#8가지 방향에 대한 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

#현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction + 1) % 8

result = 0 #최종 결과

#현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

#모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array, now_x, now_y):
    #1번부터 16번까지의 물고기를 차례대로 (낮을 번호부터) 확인
    for i in range(1, 17):
        #해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            #해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                #해당 방향을로 이동이 가능하다면 이동시키기
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                    direction = turn_left(direction)

#상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    #현재 방향으로 계속 이동 시키기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        #범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            #물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

#모든 경우를 탐색하기 위한 DFS 함수
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array) #리스트를 통째로 복사

    total += array[now_x][now_y][0] #현재 위치 물고기 먹기
    array[now_x][now_y][0] = -1 #물고기를 먹었으므로 번호 값을 -1로 반환

    move_all_fishes(array, now_x, now_y) #전체 물고기 이동

    #다시 상어가 이동할 차례이므로 이동 가능 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    #이동할 수 있는 위치가 없으면 종료
    if len(positions) == 0:
        result = max(result, total)
        return
    #모든 이동할 수 있는 위치로 재귀적으로 수행ㅇ
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

dfs(array, 0, 0, 0)
print(result)